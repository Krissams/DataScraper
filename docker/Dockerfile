FROM php:7.3.3-fpm-alpine3.9
LABEL Maintainer="Janssens Field Services <dev.support@eastvantage-europe.com>" \
      Description="Alpine 3.9 PHP 7.3 Nginx container for Laravel WebClient." \
      Version="1.0"

# Install nginx and supervisor
RUN apk update && \
    apk upgrade && \
    apk --no-cache add \
        nginx \
        supervisor && \
    rm /var/cache/apk/*

# Configure nginx
COPY config/nginx.conf /etc/nginx/nginx.conf

# Configure PHP-FPM
COPY config/fpm-pool.conf /etc/php7/php-fpm.d/www.conf
COPY config/php.ini /etc/php7/conf.d/custom.ini

# Configure supervisord
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Generate self-certificate
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/localhost.key -out /etc/ssl/certs/localhost.crt -subj "/C=PH/ST=Taguig/L=Metro Manila/O=SOP/OU=IT Department/CN=localhost"

# Create sop user
RUN adduser --disabled-password --gecos '' sop && \
    echo ' sop ALL=NOPASSWD:   ALL' >> /etc/sudoers

# Make sure files/folders needed by the processes are accessible when they run under the nobody user
RUN chown -R sop:sop /run && \
    chown -R sop:sop /var/lib/nginx && \
    chown -R sop:sop /var/tmp/nginx && \
    chown -R sop:sop /var/log/nginx && \
    chown sop:sop /etc/ssl/private/localhost.key /etc/ssl/certs/localhost.crt

# Switch to use a non-root user from here on
USER sop

# Setup document root
RUN mkdir -p /var/www

# Add application
WORKDIR /var/www

# Expose the port nginx is reachable on
EXPOSE 10001

# Let supervisord start nginx & php-fpm
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
#ENTRYPOINT ["/bin/sh"]

# Configure a healthcheck to validate that everything is up&running
HEALTHCHECK --timeout=10s CMD curl --silent --fail http://127.0.0.1:8080/fpm-ping
