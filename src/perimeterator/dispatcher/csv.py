import logging
import csv


class Dispatcher(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def dispatch(self, resources):
        self.logger.info(
            "Attempting to enqueue %d resources", len(resources),
        )

        with open('list.csv', 'a+', newline='') as csvfile:
            fieldnames = ['identifier', 'service', 'cname', 'ips']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for resource in resources:

                if not resource['addresses']:
                    continue

                writer.writerow({
                    'identifier': resource['identifier'],
                    'service': resource['service'],
                    'cname': resource['cname'],
                    'ips': ';'.join(resource['addresses']),
                })

                self.logger.info(
                    "Enqueued IPs for resource %s",
                    resource["identifier"]
                )
