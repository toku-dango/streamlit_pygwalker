
# Streamlit Pygwalker App

This repository contains a Streamlit application that allows users to upload CSV files and visualize them using Pygwalker. The app provides an intuitive interface for selecting and displaying CSV files, making it easy to explore data visually.

## Features

- Upload multiple CSV files via the sidebar.
- Select a file from the uploaded list to display its content.
- Visualize data using Pygwalker directly within the Streamlit app.
- Error handling for file upload and parsing.

## Files

- `main.py`: The main Streamlit application script.
- `config.toml`: Configuration file for setting up Streamlit (optional, depending on your deployment needs).
- `launch.bat`: Batch file for launching the application on Windows.

## Requirements

- Python 3.x
- Streamlit
- pandas
- pygwalker

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/streamlit-pygwalker-app.git
   cd streamlit-pygwalker-app
   ```

2. Install the required Python packages:
   ```sh
   pip install streamlit pandas pygwalker
   ```

## Usage

1. Run the Streamlit app:
   ```sh
   streamlit run main.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Use the sidebar to upload one or more CSV files.

4. Select a file from the dropdown menu to display and visualize its data.

## Configuration

You can customize the Streamlit configuration by modifying the `config.toml` file. Refer to the [Streamlit documentation](https://docs.streamlit.io/library/advanced-features/configuration) for more details on available configuration options.

## Launching on Windows

You can use the provided `launch.bat` file to start the application on a Windows system. Simply double-click the `launch.bat` file to run the app.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
