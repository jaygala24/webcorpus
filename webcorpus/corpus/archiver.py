
import shutil
import os
import tempfile
import tarfile
from pathlib import Path


def tmpfile_path():
    tmp_name = next(tempfile._get_candidate_names())
    tmp_dir = tempfile._get_default_tempdir()
    return os.path.join(tmp_dir, tmp_name)


class Archiver:

    def __init__(self, corpus, **options):
        self.corpus = corpus

    def archive(self):
        raise NotImplementedError


class SFArchiver(Archiver):

    def archive(self):
        tmp_path = tmpfile_path() + '.tar.xz'
        print('Archiving {} to {}'.format(self.corpus.root_path, tmp_path))
        tar = tarfile.open(tmp_path, 'w:xz')
        tar.add(self.corpus.root_path)
        tar.close()
        return tmp_path


class MFArchiver(Archiver):

    def archive(self):
        basename = os.path.basename(self.corpus.root_path)
        archive_path = os.path.join('/tmp', basename + '.tar.xz')
        print('Archiving {} to {}'.format(self.corpus.root_path, archive_path))
        tar = tarfile.open(archive_path, 'w:xz')
        tar.add(self.corpus.root_path, arcname=basename)
        tar.close()
        return archive_path