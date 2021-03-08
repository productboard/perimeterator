import logging
import csv


class Dispatcher(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.fieldnames = ['service', 'identifier', 'cname', 'ips']

        with open('list.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()

    def dispatch(self, resources):
        self.logger.info(
            "Attempting to enqueue %d resources", len(resources),
        )

        with open('list.csv', 'a+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)

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
