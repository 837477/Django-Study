#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv


dotenv.load_dotenv(
    dotenv_path=None,  # .env 파일의 절대경로 및 상대경로
    stream=None,  # .env 파일 내용에 대한 StringIO 객체
    verbose=True,  # .env 파일 누락 등의 경고 메시지를 출력할 것인지의 여부
    override=False  # .env 파일에서 정의한 환경변수가 시스템 환경변수를 덮어쓸지에 대한 여부
    # **kwargs
)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
