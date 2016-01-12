app_name=delssajri/tornado
mk_tornado_file=.tornado.timestamp

install: $(mk_tornado_file)

$(mk_tornado_file): Dockerfile
	@docker build -t $(app_name) . && touch $(mk_tornado_file)

clean:
	docker rmi -f ${app_name} > /dev/null 2>&1 || /bin/true
	rm -f $(mk_tornado_file)


