#!/bin/bash

mkdir tempdir

cp sample_app.py tempdir/.
cp -r release/* tempdir/release/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./release /home/myapp/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python /home/myapp/sample_app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t testapp .
docker run -t -d -p 5050:5050 --name qictbello testapp
docker ps -a 
