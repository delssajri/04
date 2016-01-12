app_name=delssajri/couchdb
mk_couchdb_file=.couchdb.timestamp

install: $(mk_couchdb_file)

$(mk_couchdb_file): Dockerfile
	@docker build -t $(app_name) . && touch $(mk_couchdb_file)

clean:
	docker rmi -f ${app_name} > /dev/null 2>&1 || /bin/true
	rm -f $(mk_couchdb_file)


