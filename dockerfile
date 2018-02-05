FROM monroe/base:web


WORKDIR /opt/monroe/
RUN npm install --production

COPY files/browsertime-master /opt/monroe/
COPY files/run_experiment.py /opt/monroe/
COPY files/seleniumRunner.js /opt/monroe/lib/core
COPY files/browsertime.py /opt/monroe/
COPY files/start.sh /opt/monroe/start.sh

ENTRYPOINT ["dumb-init", "--", "/usr/bin/bash", "/opt/monroe/start.sh"]
