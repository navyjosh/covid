from django.core.management.base import BaseCommand, CommandError
from covid.settings import BASE_DIR
import os
import pandas as pd
import urllib.request
from urllib.parse import quote_plus
from Bio import SeqIO
from epicov.models import Epicov
from sqlalchemy import create_engine


class Command(BaseCommand):
    help = 'Updates the Database with new data.  Make sure that you have added appropriate files before running this ' \
           'command.'

    def handle(self, *args, **kwargs):
        try:
            data_dir = os.path.join(BASE_DIR, 'raw')
            files = os.listdir(data_dir)
            meta_data_url = "https://github.com/nextstrain/ncov/blob/master/data/metadata.tsv?raw=true"
            fn = os.path.join(data_dir, 'metadata.tsv')
            urllib.request.urlretrieve(meta_data_url, fn)
            metadata = pd.read_csv(fn, delimiter='\t')
            fn = None
            for file in files:
                if ".fasta" in file:
                    fn = os.path.join(BASE_DIR, 'raw', file)
                    break
            if fn:
                engine = create_engine('postgresql://covid:%s@localhost:5432/covid' % quote_plus('nutrit1on+'))
                with open(fn, 'r') as fh:
                    missing_epi = []
                    i = 0
                    for record in SeqIO.parse(fh, "fasta"):
                        i += 1
                        try:
                            gisaid_epi_isl = record.id.split("|")[-2]
                            record_id = record.id
                            seq = str(record.seq)
                            pd.Series({'ident': record_id, 'seq': seq}).append(metadata.loc[metadata.gisaid_epi_isl == gisaid_epi_isl]).to_sql('covid', engine, if_exists='append')
                            self.stdout.write('Wrote Record ID: %s to database')

                        except Exception as e:
                            self.stdout.write(str(e))
                        if i >= 10: break
        except Exception as e:
            self.stdout.write(str(e))


            df = pd.DataFrame









