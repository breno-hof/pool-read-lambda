locals {
	lambda_name			= "pool-read"
	handler_entrypoint	= "app.lambda_handler"
	timeout				= 300
	runtime				= "python3.12"
	source_path			= "../src/"
}