from similar_articles.configuration import Configuration
from similar_articles.service.s3 import S3
from similar_articles.datasource.references_datasource import ReferencesDataSource
from similar_articles.model.gensim_word2vec import GensimWord2Vec
import logging


if __name__ == "__main__":

    logging.basicConfig(
        format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
    )

    logging.info('loading configuration files')
    model_config = Configuration("configs/model_config.json").parameters
    aws_config = Configuration("configs/aws_config.json").parameters

    s3 = S3(**aws_config["s3"])

    key, filename = (
        model_config["references_data"].split("/")[1],
        model_config["references_data"],
    )
    logging.info('loading references data from S3')
    s3.download(key, filename)

    references_data = ReferencesDataSource(model_config["references_data"]).transform()

    model = GensimWord2Vec(model_config["model"])
    logging.info('training model')
    model.fit(references_data)
    logging.info('saving model to disk')
    model.save(model_config["output_path"])

    logging.info('uploading embeddings to S3')
    filename, key = model_config["output_path"], model_config["output_path"].split('/')[1]
    s3.upload(filename, key)