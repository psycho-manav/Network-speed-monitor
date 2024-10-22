## 🛜 Network Speed Monitor

This Python app displays **real-time network speed** (upload and download) in **MB/s**, using `psutil` to track network traffic and `matplotlib` for live graph plotting. There's also an optional **Tkinter GUI** version for a simple boring window.

## 📸 Preview (Graph Version)
This silly app tracks your network activity and updates every second, giving you a 60-second sliding window view of upload and download speeds.

---

## 🛠️ Features
- 📊 **Live graph** showing real-time **upload/download speeds**.
- 📈 60-second **sliding window** graph.
- 🖥️ Optional **Tkinter GUI version** for a simple app window.
- 🧑‍💻 Create an executable using **PyInstaller** for easy sharing.

---

## 🚀 How to Run the Program
### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/Network-Speed-Monitor.git
cd Network-Speed-Monitor
```

---

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install psutil matplotlib
```

---

### 3. Run the App
For the **graph version**:
```bash
python network_speed_monitor.py

```

For the **Tkinter GUI version**:
```bash
python network_speed_gui.py
```

---

## 🛑 Troubleshooting
- **Matplotlib issues?** Make sure `matplotlib` is installed. Run:
  ```bash
  pip install matplotlib
  ```
- **Network speeds stuck at zero?** Ensure you are connected to a network and not behind strict firewalls.

---

## 💻 How to Package the App (Optional)
If you want to **share the app** as an executable (e.g., `.exe` on Windows), use **PyInstaller**:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed network_speed_monitor.py
```
After running this command, the executable will be available in the `dist/` folder.

---

## 👀 Preview of the Tkinter GUI
The Tkinter version provides a minimal window with live upload and download speed updates.

```plaintext
Download Speed: 2.45 MB/s
Upload Speed: 0.89 MB/s
```

---

## 🎉 Flex Time: Share and Contribute!
If you found this project fun, **give it a star ⭐** on GitHub.  
Feel free to **fork** the repository, make improvements, or submit **pull requests**! 

---

## 📄 License
This project is licensed under the MIT License - feel free to modify or share it.

---

## 🤝 Contributions
- **Contributions are welcome!** Open an issue or submit a pull request if you have ideas for improvements or new features.
- Add a 💬 comment in the **Discussions** section if you want to chat about the project.

---

## 🧑‍🏫 Author  
Built with ❤️ by **manav**.  
If you liked it, don’t forget to flex this ridiculous creation with your friends! 😎

---

## 🔗 Links
- [GitHub Repository](https://github.com/psycho-manav/Network-speed-monitor)
