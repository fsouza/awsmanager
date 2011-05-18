test:
	@specloud --with-coverage --cover-package=awsmanager --cover-erase

clean:
	@find . -name "*.pyc" -exec rm -f {} \;
