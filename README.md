## AWS Lambda with serverless framework

This code in this repository is explained in this Medium Article.

- This repository contains examples of [AWS lambda function ](https://aws.amazon.com/lambda/ "AWS lambda function ")attached to S3, API Gateway, SNS topic.
- The code uses [Serverless Framework](https://www.serverless.com/ "Serverless Framework") to deploy the lambda functions and managing the infrastructure.
- The code use [serverless-secrets-plugin](https://github.com/serverless/serverless-secrets-plugin "serverless-secrets-plugin") to manage code configuration and secrets.

### Installation
- Install docker on your machine. You can follow the steps mentioned in this official [docker installation link.](https://docs.docker.com/engine/install/ "docker installation link.")
- Next we need to install serverless framework. It requires nodejs already installed on your machine as serverless framework is written in nodejs. To install nodejs on your machine follow this [nodejs installation guide](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04 "nodejs installation guide") by digital ocean.
- Once both nodejs and NPM are installed, we can install serverless framework by running the following command. 

     `npm install -g serverless`
- Then setup your AWS credentials for serverless framework to access your AWS, follow this [official setup by serverless](https://www.serverless.com/framework/docs/providers/aws/guide/credentials "official setup by serverless").

### Deploying the code
- The repository contains three folder with each for S3, API Gateway and SNS topic.
- Change your working directory to any one of them and install the following plugins required by serverless. (Note: you must have a secret.live.yml which contains all the secrets and configurations used in the code.)

    `sls plugin install -n serverless-python-requirements`
	
    ` npm install serverless-secrets-plugin`

- Since the examples are written in python you will need virtual environment for python and i preferably use venv. Link to [setup](https://docs.python.org/3/tutorial/venv.html "setup") venv on your machine.
- create your virtual environment using the following command and activate it using next command.

    `python3 -m venv env`

    `source env/bin/activate`

- To deploy your lambda function run the following command

   `sls deploy`


