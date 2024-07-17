# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Praedictiva <felipe.macias@gmail.com>" \
      org.label-schema.name="nexus-varnish" \
      org.label-schema.description="Nexus Varnish image." \
      org.label-schema.vendor="Praedictiva"

COPY etc/varnish.vcl /etc/varnish/default.vcl
