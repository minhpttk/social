# Sử dụng image Python 3.10
FROM python:3.10

# Thiết lập thư mục làm việc
WORKDIR /usr/src/app

# Cài đặt pipenv
RUN pip install pipenv

# Sao chép Pipfile và Pipfile.lock vào thư mục làm việc
COPY Pipfile Pipfile.lock ./

# Cài đặt các phụ thuộc
RUN pipenv install --system --deploy

# Sao chép toàn bộ dự án vào thư mục làm việc
COPY . .

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

# Môi trường và cổng
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
