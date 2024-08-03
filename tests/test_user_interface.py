import unittest
import tkinter as tk
from src.user_interface import create_ui

class TestUserInterface(unittest.TestCase):
    
    def setUp(self):
        """Set up the GUI for testing."""
        self.root = tk.Tk()
        self.ui = create_ui(self.root)
        self.root.update()  # Update the root to ensure the UI components are rendered
    
    def tearDown(self):
        """Destroy the GUI after testing."""
        self.root.destroy()
    
    def test_create_ui(self):
        """Test if the UI is created and contains essential elements."""
        # Check if the main window is not None
        self.assertIsNotNone(self.ui)
        
        # Check if buttons are present in the UI
        self.assertTrue(any(widget.cget("text") == "Import CSV" for widget in self.root.winfo_children() if isinstance(widget, tk.Button)))
        self.assertTrue(any(widget.cget("text") == "Export CSV" for widget in self.root.winfo_children() if isinstance(widget, tk.Button)))
        
        # Check if the UI has a layout (e.g., grid, pack)
        for widget in self.root.winfo_children():
            self.assertIsNotNone(widget.grid_info() or widget.pack_info(), "Widget should have a layout")
    
    def test_import_csv_button(self):
        """Test if the Import CSV button works correctly."""
        import_button = next((widget for widget in self.root.winfo_children() if isinstance(widget, tk.Button) and widget.cget("text") == "Import CSV"), None)
        self.assertIsNotNone(import_button)
        
        # Simulate a button click and check if the action is performed (you need to define expected behavior in `create_ui`)
        import_button.invoke()
        # Add assertions here based on expected behavior (e.g., checking if a file dialog appears)
    
    def test_export_csv_button(self):
        """Test if the Export CSV button works correctly."""
        export_button = next((widget for widget in self.root.winfo_children() if isinstance(widget, tk.Button) and widget.cget("text") == "Export CSV"), None)
        self.assertIsNotNone(export_button)
        
        # Simulate a button click and check if the action is performed (you need to define expected behavior in `create_ui`)
        export_button.invoke()
        # Add assertions here based on expected behavior (e.g., checking if a file dialog appears)
    
if __name__ == "__main__":
    unittest.main()
