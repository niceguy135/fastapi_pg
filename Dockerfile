FROM python:3.12-slim as build

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

FROM nginx:stable-alpine
COPY --from=build nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]
CMD ["python", "src/main.py", "--prepare-db"]
CMD ["python", "src/main.py"]