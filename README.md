# 🔐 Password Manager (Python + Tkinter)

A simple and secure **Password Manager desktop application** built using **Python** and **Tkinter**.
It allows users to generate strong passwords, save login credentials securely in a JSON file, and retrieve them easily when needed.

---

## 📌 Features

* 🔑 **Strong Password Generator**

  * Random combination of letters, numbers, and symbols
  * Automatically copies password to clipboard

* 💾 **Secure Storage**

  * Saves credentials locally in a `data.json` file
  * Stores website, email/username, and password

* 🔍 **Search Functionality**

  * Retrieve saved credentials by website name

* 🖥️ **User-Friendly GUI**

  * Built using Tkinter
  * Clean and simple interface

* ⚠️ **Error Handling**

  * Handles missing files
  * Prevents saving empty fields

---

## 📸 Screenshots

### 🖥️ Main Interface

<img width="774" height="615" alt="image" src="https://github.com/user-attachments/assets/dbed68e4-fddf-4cc7-8920-7c1aaf415c43" />


### 🔑 Password Generation

<img width="769" height="648" alt="image" src="https://github.com/user-attachments/assets/24ab1499-611c-4f7e-a6c3-02374b96bab1" />


### 🔍 Search Result

<img width="755" height="639" alt="image" src="https://github.com/user-attachments/assets/0c9237e9-1cab-4c70-88b1-0084af2464e0" />


---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI framework
* **JSON** – Data storage
* **pyperclip** – Clipboard support
* **random module** – Password generation

---

## 📂 Project Structure

```
Password-Manager/
│
├── main.py
├── data.json
├── logo.png
├── screenshots/
│   ├── screenshot-main.png
│   ├── screenshot-password-generated.png
│   └── screenshot-search.png
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/password-manager.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd password-manager
```

### 3️⃣ Install Required Module

```bash
pip install pyperclip
```

### 4️⃣ Run the Application

```bash
python main.py
```

---

## 🧪 How It Works

1. Enter the **website name**
2. Enter your **email/username**
3. Click **Generate Password** (optional)
4. Click **Add** to save credentials
5. Use **Search** to retrieve saved passwords

---

## 🔐 Data Storage

* All credentials are stored locally in `data.json`
* No internet connection required
* No data is shared externally

---

## 🚀 Future Improvements

* Encrypt stored passwords
* Add update/delete credential feature
* Add master password authentication
* Dark mode UI

---

## 👨‍💻 Author

**Piyush Pal**
Computer Science Engineering Graduate

---

## ⭐ Acknowledgements

Inspired by **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

---

## 📜 License

This project is licensed under the **MIT License**.

---


