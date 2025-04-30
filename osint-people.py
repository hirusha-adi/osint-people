import click
import typing as t
import modules
from utils.initialize import initialize
from utils import decorators

# ---------------------------------------------------------------------------
# Initialize Stuff
# ---------------------------------------------------------------------------

@click.command('init')
def init() -> None:
    initialize()


# ---------------------------------------------------------------------------
# Emails
# ---------------------------------------------------------------------------

@click.group()
def email():
    pass

@email.command('holehe')
@click.option('--email', required=True, help='Email address')
@click.option('--color', is_flag=True, default=False, help='Enable color output')
@click.option('--clear', is_flag=True, default=False, help='Clear the output')
@decorators.show_function_info
def email_holehe(email: str, color: bool = False, clear: bool = False) -> None:
    print(f"Running email holehe with email: {email}")
    modules.email.holehe_.start(email, color=color, clear=clear)

@email.command('specific/chess_com')
@decorators.show_function_info
@click.option('--email', required=True, help='Email address')
def email_specific_chess_com(email: str) -> None:
    modules.email.specific.chess_com.start(email)

@email.command('specific/deezer')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__deezer(email: str) -> None:
    modules.email.specific.deezer.start(email)

@email.command('specific/duolingo')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__duolingo(email: str) -> None:
    modules.email.specific.duolingo.start(email)

@email.command('specific/github')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__github(email: str) -> None:
    modules.email.specific.github.start(email)

@email.command('specific/gravatar')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__gravatar(email: str) -> None:
    modules.email.specific.gravatar.start(email)

@email.command('specific/imgur')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__imgur(email: str) -> None:
    modules.email.specific.imgur.start(email)

@email.command('specific/instagram')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__instagram(email: str) -> None:
    modules.email.specific.instagram.start(email)

@email.command('specific/pinterest')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__pinterest(email: str) -> None:
    modules.email.specific.pinterest.start(email)

@email.command('specific/pornhub')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__pornhub(email: str) -> None:
    modules.email.specific.pornhub.start(email)

@email.command('specific/spotify')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__spotify(email: str) -> None:
    modules.email.specific.spotify.start(email)

@email.command('specific/strava')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__strava(email: str) -> None:
    modules.email.specific.strava.start(email)

@email.command('specific/twitter')
@click.option('--email', required=True, help='Email address')
@decorators.show_function_info
def email_specific__twitter(email: str) -> None:
    modules.email.specific.twitter.start(email)


# ---------------------------------------------------------------------------
# Passwords
# ---------------------------------------------------------------------------

@click.group()
def password():
    pass

@password.command('pastebin')
@click.option('--password', required=True, help='Password')
@decorators.show_function_info
def password_pastebin(password: str) -> None:
    modules.password.pastebin.start(password)

@password.command('haveibeenpwned/breach_info')
@click.option('--breach', required=True, help='Breach identifier')
@decorators.show_function_info
def password_haveibeenpwned_breach_info(breach: str) -> None:
    modules.password.haveibeenpwned.breach_info.start(breach)

@password.command('haveibeenpwned/check')
@click.option('--password', required=True, help='Password')
@decorators.show_function_info
def password_haveibeenpwned_check(password: str) -> None:
    modules.password.haveibeenpwned.check.start(password)

@password.command('haveibeenpwned/domain_check')
@click.option('--domain', required=True, help='Domain')
@decorators.show_function_info
def password_haveibeenpwned_domain_check(domain: str) -> None:
    modules.password.haveibeenpwned.domain_check.start(domain)

@password.command('haveibeenpwned/domains_list')
@click.option('--domains', required=True, help='Domains List')
@decorators.show_function_info
def password_haveibeenpwned_domains_list(domains: str) -> None:
    modules.password.haveibeenpwned.domains_list.start(domains)

@password.command('haveibeenpwned/filtered_check')
@click.option('--email', required=True, help='Email Address')
@click.option('--domain', required=True, help='Domain')
@decorators.show_function_info
def password_haveibeenpwned_filtered_check(email: str, domain: str) -> None:
    modules.password.haveibeenpwned.filtered_check.start(email=email, domain=domain)

@password.command('haveibeenpwned/range')
@click.option('--password', required=True, help='Password')
@decorators.show_function_info
def password_haveibeenpwned_range(password: str) -> None:
    modules.password.haveibeenpwned.range_.start(password)


# ---------------------------------------------------------------------------
# Phone Numbers
# ---------------------------------------------------------------------------

@click.group()
def phonenumber():
    pass

@phonenumber.command('phoneinfoga/dorks')
@click.option('--number', required=True, help='Phone number')
@decorators.show_function_info
def phonenumber_phoneinfoga_dorks(number: str) -> None:
    modules.phonenumber.phoneinfoga.dorks.start(number)

@phonenumber.command('phoneinfoga/search')
@click.option('--number', required=True, help='Phone number')
@decorators.show_function_info
def phonenumber_phoneinfoga_search(number: str) -> None:
    modules.phonenumber.phoneinfoga.search.start(number)

# ---------------------------------------------------------------------------
# Usernames
# ---------------------------------------------------------------------------

@click.group()
def username():
    pass

@username.command('search/lookup')
@click.option('--username', required=True, help='Username')
@decorators.show_function_info
def username_search_lookup(username: str) -> None:
    modules.username.search.lookup.start(username)

@username.command('search/directory')
@click.option('--username', required=True, help='Username')
@decorators.show_function_info
def username_search_directory(username: str) -> None:
    modules.username.search.directory.start(username)

@username.command('specific/amazon')
@click.option('--username', required=True, help='Username')
@decorators.show_function_info
def username_specific_amazon(username: str) -> None:
    modules.username.specific.amazon.start(username)

@username.command('specific/github')
@click.option('--username', required=True, help='Username')
@decorators.show_function_info
def username_specific_github(username: str) -> None:
    modules.username.specific.github.start(username)


if __name__ == '__main__':
    @click.group()
    def osint_people():
        pass

    osint_people.add_command(init)
    osint_people.add_command(email)
    osint_people.add_command(password)
    osint_people.add_command(phonenumber)
    osint_people.add_command(username)

    osint_people()
