# Access Granted - The System 

A retro-style command line interface inspired by the cool terminal interfaces seen in movies and TV shows.

## Motivation 

I've always been fascinated by those sleek, dramatic CLI interfaces you see in movies and TV shows - you know, the ones where hackers and tech experts interact with mysterious systems through green text on black screens, complete with ASCII art and dramatic "ACCESS GRANTED" messages. This project is my attempt to recreate that cinematic experience!

Whether it's the computer interfaces in *The Matrix*, *TRON*, *WarGames*, or countless sci-fi thrillers, there's something undeniably cool about those terminal-based systems. So I decided to build my own version of "The System" - a simple but atmospheric CLI that captures that retro-futuristic vibe.

## Features 

- **ASCII Art Welcome Screen**: Displays "The System" in stylized ASCII art
- **Password Authentication**: Simple password protection (because every good movie system needs one!)
- **Retro Styling**: Clean, minimalist interface that feels like something from a 1980s sci-fi film
- **Access Granted Animation**: Satisfying confirmation when you successfully authenticate

## Installation 

1. Clone this repository:
   ```bash
   git clone https://github.com/israelo19/codespaces-blank.git
   cd codespaces-blank
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install InquirerPy art
   ```

## Usage 

Run the system:
```bash
python system.py
```

Enter the password when prompted (hint: it's `abc`) and enjoy the retro terminal experience!

## Dependencies 

- `art` - For generating ASCII art text
- `InquirerPy` - For enhanced CLI interactions (ready for future features)


## Inspiration 

This project draws inspiration from classic computer interfaces in:
- The Matrix (1999)
- TRON (1982)
- WarGames (1983)
- Hackers (1995)
- And countless other sci-fi movies and TV shows

## Contributing 

If you share the same fascination with retro CLI interfaces and want to help make "The System" even cooler, feel free to:
- Submit feature requests
- Report bugs
- Contribute code improvements
- Suggest new movie-inspired features

## License 

This project is open source and available under the MIT License.

---

*"Access Granted" - The System*

Built with ❤️ and a love for retro computing aesthetics.
