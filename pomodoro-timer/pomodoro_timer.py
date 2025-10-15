"""
Pomodoro Timer - Productivity timer with breaks
Features:
- 25-minute work sessions
- 5-minute short breaks
- 15-minute long breaks after 4 sessions
- Visual countdown timer
- Sound notifications
- Session tracking
- Statistics and productivity reports
"""

import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime
import json
import os

try:
    import winsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("🍅 Pomodoro Timer")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#2C3E50')
        
        # Timer settings (in seconds)
        self.WORK_TIME = 25 * 60  # 25 minutes
        self.SHORT_BREAK = 5 * 60  # 5 minutes
        self.LONG_BREAK = 15 * 60  # 15 minutes
        
        # Timer state
        self.time_left = self.WORK_TIME
        self.is_running = False
        self.is_work_session = True
        self.sessions_completed = 0
        self.timer_id = None
        
        # Statistics file
        self.stats_file = "pomodoro_stats.json"
        
        # Create UI
        self.create_widgets()
        self.load_stats()
        self.update_display()
    
    def create_widgets(self):
        """Create all UI widgets"""
        
        # Title
        title_label = tk.Label(
            self.root,
            text="🍅 POMODORO TIMER",
            font=('Helvetica', 24, 'bold'),
            bg='#2C3E50',
            fg='#ECF0F1'
        )
        title_label.pack(pady=20)
        
        # Session info
        self.session_label = tk.Label(
            self.root,
            text="Work Session",
            font=('Helvetica', 18),
            bg='#2C3E50',
            fg='#E74C3C'
        )
        self.session_label.pack(pady=10)
        
        # Timer display
        self.timer_frame = tk.Frame(self.root, bg='#34495E', bd=5, relief='ridge')
        self.timer_frame.pack(pady=20, padx=50, fill='both', expand=True)
        
        self.timer_label = tk.Label(
            self.timer_frame,
            text="25:00",
            font=('Courier', 60, 'bold'),
            bg='#34495E',
            fg='#ECF0F1'
        )
        self.timer_label.pack(pady=40)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            self.root,
            length=400,
            mode='determinate',
            style='Custom.Horizontal.TProgressbar'
        )
        self.progress.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg='#2C3E50')
        button_frame.pack(pady=20)
        
        # Start/Pause button
        self.start_button = tk.Button(
            button_frame,
            text="▶ START",
            command=self.toggle_timer,
            font=('Helvetica', 14, 'bold'),
            bg='#27AE60',
            fg='white',
            width=12,
            height=2,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        self.start_button.grid(row=0, column=0, padx=10)
        
        # Reset button
        reset_button = tk.Button(
            button_frame,
            text="⟲ RESET",
            command=self.reset_timer,
            font=('Helvetica', 14, 'bold'),
            bg='#E67E22',
            fg='white',
            width=12,
            height=2,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        reset_button.grid(row=0, column=1, padx=10)
        
        # Skip button
        skip_button = tk.Button(
            button_frame,
            text="⏭ SKIP",
            command=self.skip_session,
            font=('Helvetica', 14, 'bold'),
            bg='#3498DB',
            fg='white',
            width=12,
            height=2,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        skip_button.grid(row=0, column=2, padx=10)
        
        # Statistics frame
        stats_frame = tk.Frame(self.root, bg='#34495E', bd=3, relief='ridge')
        stats_frame.pack(pady=20, padx=50, fill='x')
        
        stats_title = tk.Label(
            stats_frame,
            text="📊 Today's Statistics",
            font=('Helvetica', 14, 'bold'),
            bg='#34495E',
            fg='#ECF0F1'
        )
        stats_title.pack(pady=5)
        
        self.stats_label = tk.Label(
            stats_frame,
            text="Sessions: 0 | Total Time: 0 min",
            font=('Helvetica', 12),
            bg='#34495E',
            fg='#ECF0F1'
        )
        self.stats_label.pack(pady=5)
        
        # Configure progress bar style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'Custom.Horizontal.TProgressbar',
            troughcolor='#34495E',
            background='#27AE60',
            thickness=20
        )
    
    def toggle_timer(self):
        """Start or pause the timer"""
        if self.is_running:
            self.pause_timer()
        else:
            self.start_timer()
    
    def start_timer(self):
        """Start the timer"""
        self.is_running = True
        self.start_button.config(text="⏸ PAUSE", bg='#E67E22')
        self.countdown()
    
    def pause_timer(self):
        """Pause the timer"""
        self.is_running = False
        self.start_button.config(text="▶ RESUME", bg='#27AE60')
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
    
    def countdown(self):
        """Countdown timer logic"""
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
            self.timer_id = self.root.after(1000, self.countdown)
        elif self.time_left == 0:
            self.session_complete()
    
    def update_display(self):
        """Update timer display and progress bar"""
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        
        # Update progress bar
        if self.is_work_session:
            total_time = self.WORK_TIME
        elif self.sessions_completed % 4 == 0 and self.sessions_completed > 0:
            total_time = self.LONG_BREAK
        else:
            total_time = self.SHORT_BREAK
        
        progress_value = ((total_time - self.time_left) / total_time) * 100
        self.progress['value'] = progress_value
    
    def session_complete(self):
        """Handle session completion"""
        self.is_running = False
        self.play_sound()
        
        if self.is_work_session:
            # Work session completed
            self.sessions_completed += 1
            self.save_session()
            self.update_stats_display()
            
            # Determine break type
            if self.sessions_completed % 4 == 0:
                # Long break
                self.time_left = self.LONG_BREAK
                self.session_label.config(text="Long Break", fg='#9B59B6')
                messagebox.showinfo(
                    "Break Time!",
                    f"Great work! Session {self.sessions_completed} complete!\n"
                    "Take a 15-minute long break! 🎉"
                )
            else:
                # Short break
                self.time_left = self.SHORT_BREAK
                self.session_label.config(text="Short Break", fg='#3498DB')
                messagebox.showinfo(
                    "Break Time!",
                    f"Session {self.sessions_completed} complete!\n"
                    "Take a 5-minute break! ☕"
                )
            
            self.is_work_session = False
        else:
            # Break completed
            self.time_left = self.WORK_TIME
            self.session_label.config(text="Work Session", fg='#E74C3C')
            self.is_work_session = True
            messagebox.showinfo(
                "Back to Work!",
                "Break is over. Time to focus! 💪"
            )
        
        self.start_button.config(text="▶ START", bg='#27AE60')
        self.update_display()
    
    def reset_timer(self):
        """Reset the timer"""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        
        self.is_running = False
        self.is_work_session = True
        self.time_left = self.WORK_TIME
        self.session_label.config(text="Work Session", fg='#E74C3C')
        self.start_button.config(text="▶ START", bg='#27AE60')
        self.progress['value'] = 0
        self.update_display()
    
    def skip_session(self):
        """Skip current session"""
        if messagebox.askyesno("Skip Session", "Are you sure you want to skip this session?"):
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
            self.time_left = 0
            self.session_complete()
    
    def play_sound(self):
        """Play notification sound"""
        if SOUND_AVAILABLE:
            try:
                winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms
            except:
                pass
        # Alternative: print('\a') for system beep
        print('\a')
    
    def save_session(self):
        """Save completed session to stats"""
        stats = self.load_stats()
        today = datetime.now().strftime("%Y-%m-%d")
        
        if today not in stats:
            stats[today] = {'sessions': 0, 'total_minutes': 0}
        
        stats[today]['sessions'] += 1
        stats[today]['total_minutes'] += self.WORK_TIME // 60
        
        with open(self.stats_file, 'w') as f:
            json.dump(stats, f, indent=4)
    
    def load_stats(self):
        """Load statistics from file"""
        if not os.path.exists(self.stats_file):
            return {}
        try:
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def update_stats_display(self):
        """Update statistics display"""
        stats = self.load_stats()
        today = datetime.now().strftime("%Y-%m-%d")
        
        if today in stats:
            sessions = stats[today]['sessions']
            total_minutes = stats[today]['total_minutes']
            self.stats_label.config(
                text=f"Sessions: {sessions} | Total Time: {total_minutes} min"
            )
        else:
            self.stats_label.config(text="Sessions: 0 | Total Time: 0 min")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    app.run()
