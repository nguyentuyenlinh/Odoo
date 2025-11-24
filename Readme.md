# Hướng Dẫn Cài Đặt Odoo với Docker (Có Debug)

## 📋 Tổng Quan

Repository này cung cấp cách dễ dàng để chạy Odoo 18 với Docker, bao gồm cả tính năng debug Python.

## 🚀 Cài Đặt Nhanh

### Yêu cầu hệ thống

-   Docker Desktop
-   VS Code (cho debug)
-   Python extension trong VS Code

### Các bước cài đặt

1. **Clone repository:**

    ```bash
    git clone https://github.com/PhucChiVas161/odoo-erp-docker.git
    cd odoo-erp-docker
    ```

2. **Chạy Odoo:**

    ```bash
    docker-compose up -d
    ```

3. **Truy cập Odoo:**
    - URL: `http://localhost:8069`
    - Tài khoản: `admin` / `admin`

## 🐛 Hướng Dẫn Debug

### Chuẩn bị môi trường debug

1. **Cài đặt Python extension trong VS Code**

    - Mở VS Code
    - `Ctrl+Shift+X` → Tìm "Python" → Install

2. **Tạo cấu hình debug**

    - `Ctrl+Shift+D` (Run and Debug)
    - Click "create a launch.json file"
    - Chọn "Python"
    - Thay thế nội dung file `.vscode/launch.json`:

    ```json
    {
        "version": "0.2.1",
        "configurations": [
            {
                "name": "Attach to Odoo",
                "type": "debugpy",
                "request": "attach",
                "connect": {
                    "host": "localhost",
                    "port": 5678
                },
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}/addons",
                        "remoteRoot": "/mnt/extra-addons"
                    }
                ]
            }
        ]
    }
    ```

### Quy trình debug

1. **Đặt breakpoint:**

    - Mở file code Python (ví dụ: `addons/custom_modules/models/debug_test.py`)
    - Click vào số dòng bên trái để đặt breakpoint

2. **Attach debugger:**

    - Trong VS Code, chọn "Attach to Odoo" → Nhấn F5
    - Chờ thông báo "Debugger attached"

3. **Start Odoo:**

    ```bash
    docker-compose up -d
    ```

4. **Test debug:**
    - Truy cập `http://localhost:8069`
    - Vào Custom → Debug Test
    - Tạo record mới hoặc click button để trigger code
    - Breakpoint sẽ dừng lại trong VS Code

### Module debug mẫu

Repository bao gồm module `custom_modules` với model `debug.test` để test debug:

-   **File:** `addons/custom_modules/models/debug_test.py`
-   **Breakpoints có thể đặt:**
    -   Dòng tính `computed_value`
    -   Method `action_debug`

## 🔧 Lệnh hữu ích

```bash
# Start containers
docker-compose up -d

# Stop containers
docker-compose down

# View logs
docker-compose logs -f web

# Restart Odoo
docker-compose restart web

# Reset database
docker-compose down -v
docker-compose up -d
```

## 📁 Cấu trúc thư mục

```
odoo-erp-docker/
├── docker-compose.yaml    # Cấu hình Docker
├── Dockerfile            # Build Odoo image
├── odoo.conf            # Cấu hình Odoo
├── addons/              # Custom modules
│   └── custom_modules/
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── debug_test.py
│       └── views/
│           └── debug_test_views.xml
└── Readme.md
```

## ❓ Xử lý sự cố

### Lỗi "Model not found"

-   Đảm bảo đã tạo `__init__.py` trong thư mục module
-   Restart containers: `docker-compose down && docker-compose up -d`

### Debug không hoạt động

-   Kiểm tra port 5678 không bị block
-   Đảm bảo Python extension đã cài
-   Restart VS Code

### Database lỗi

```bash
# Reset database
docker-compose down -v
docker-compose up -d
```

## 📞 Liên hệ

-   **GitHub:** [PhucChiVas161](https://github.com/PhucChiVas161)
-   **Email:** phucchivas161@gmail.com

---

_Chúc bạn debug hiệu quả! 🐛✨_
