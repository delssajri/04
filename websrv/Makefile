app_name=delssajri/payserver
mk_app_file=.app.timestamp
mk_tornado_file=.tornado_image.timestamp
tornado_image_dir=./tornado_image

install: $(mk_app_file)

$(mk_app_file): $(mk_tornado_file) Dockerfile
	@docker build -t $(app_name) . && touch $(mk_app_file)


$(mk_tornado_file): $(tornado_image_dir)/Dockerfile
	make install -C $(tornado_image_dir)/ && touch $(mk_tornado_file)

clean:
	docker rmi -f ${app_name} > /dev/null 2>&1 || /bin/true
	rm  -f $(mk_app_file) $(mk_tornado_file)
	make clean -C $(tornado_image_dir)/

