# OSINT People

OSINT People is an OSINT (Open Source Intelligence) tool designed to help you gather information about individuals based on various identifiers like email addresses, usernames, phone numbers, and passwords. This tool integrates with multiple OSINT services and provides several commands to gather relevant data.

## Modules

#### Username Lookup

Demonstration: [Youtube Video](https://youtu.be/wycDqyVkIdE)

![demo](./showcase/demo_user_lookup.mp4)

## Installation

### From source

1. Clone the repository:

```
git clone https://github.com/hirusha-adi/osint-people.git
cd osint-people
```

2. Enable and activate a virtual environment (optional but recommended)

```
python3 -m venv env
source env/bin/activate
```

3. Install the required dependencies:

```
pip3 install -r requirements.txt
```

4. Run the script:

```
python3 osint_people.py --help
```

### Using the executable

1. Go to the [latest release](https://github.com/hirusha-adi/osint-people/releases/latest).
2. Download the `osint_people.exe` file.
3. Open a shell (cmd/powershell) in the same directory to start using it.

You should use `osint_people.exe` instead of `python3 osint_people.py` wherever it's mentioned at.

## Usage

Make sure to run the command below to initialize all the dependencies required for all the modules to function correctly before using anything.

```
python3 osint_people.py init
```

## Usage Examples

```
python3 osint_people.py --help
```

## How it works?

Learn more here.
