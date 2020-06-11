from django.core.management.base import BaseCommand, CommandError
from covid.settings import BASE_DIR
import os
import pandas as pd
from epicov.models import Epicov



class Command(BaseCommand):
    help = 'Updates the Database with new data.  Make sure that you have added appropriate files before running this ' \
           'command.'

    def handle(self, *args, **kwargs):
        try:
            data_dir = os.path.join(BASE_DIR, 'raw')
            files = os.listdir(data_dir)
            # meta_data_url = "https://github.com/nextstrain/ncov/blob/master/data/metadata.tsv?raw=true"
            fn = os.path.join(data_dir, 'countries.csv')
            # urllib.request.urlretrieve(meta_data_url, fn)
            countries = pd.read_csv(fn)
            missing = []
            found = []
            for record in Epicov.objects.all():
                data = countries.loc[countries.name.str.lower() == record.country.strip().lower()]
                if not data.empty and record.lat is not None:
                    record.lat = float(data.latitude)
                    record.lon = float(data.longitude)
                    record.save()
                else:
                    if record.country not in missing:
                        missing.append(str(record.country))

            with open(os.path.join(data_dir, 'missing.csv'), 'w') as fh:
                fh.write(",\r\n".join(missing))
        except Exception as e:
            self.stdout.write(str(e))
