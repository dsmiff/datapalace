# Datapalace

Master dataset creation

## Getting Started

sh package was installed with Anaconda.
Otherwise it will use shutil automatically.

### Installing

```
git clone -o <target dir> git@github.com:dsmiff/datapalace.git --recursive
```

### Make a Master database

```
cd datapalace
python create_master_database.py --in-dir <dir> --filesize <filesize> --structure <name1>,<size1>,<name2>,<size1>
```

### Update a Master database

```
python update_master_database.py --in-dir <dir> --structure <name1>,<size1>
```

### Backup a Master database

```
python backup_master_database.py --in-dir <dir> --out-dir <outdir>
```


# Foursquare - WIP

Scrape data off Foursquare and find a venue for a given latitude and longitude.

### Requirements

Pandas
```
pip install pandas
```
Or create a conda environment and set it up there.

```
python data_refresh.py
```