import click
import json
import requests


def get_meraki_auth_headers(api_key):
    headers = {'X-Cisco-Meraki-API-Key': f'{api_key}'}
    return headers


def is_valid_url_and_key(api_key, base_url):
    url = f'{base_url}/api/v0/organizations'
    headers = get_meraki_auth_headers(api_key)
    try:
        res = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        return False
    return res.status_code is 200


def print_request_payload(res):
    click.echo(json.dumps(res.json(), indent=4))


@click.group()
@click.option('--api_key', prompt=True, required=True, help='Your Meraki API key')
@click.option('--base_url', prompt=True, required=True, help='The base URL for your requests (https://api.meraki.com)')
@click.pass_context
def cli(ctx, api_key, base_url):
    ctx.obj['api_key'] = api_key
    ctx.obj['base_url'] = base_url
    if not is_valid_url_and_key(api_key, base_url):
        raise click.BadParameter("Your base_url or api_key was missing or invalid")


@cli.command()
@click.option('--network_id', prompt=True, required=True, help='This is your meraki network_id')
@click.pass_context
def get_network_settings(ctx, network_id):
    url = f'{ctx.obj["base_url"]}/api/v0/networks/{network_id}/wireless/electronicShelfLabel'
    headers = get_meraki_auth_headers(ctx.obj['api_key'])
    res = requests.get(url, headers=headers)
    print_request_payload(res)


@cli.command()
@click.option('--network_id', prompt=True, required=True, help='This is your meraki network_id')
@click.option('--enabled', prompt=True, required=True, help='This is enabled/disabled')
@click.option('--host_name', prompt=True, required=True, help='This is the host name')
@click.pass_context
def edit_network_settings(ctx, network_id, enabled, host_name):
    url = f'{ctx.obj["base_url"]}/api/v0/networks/{network_id}/wireless/electronicShelfLabel'
    headers = get_meraki_auth_headers(ctx.obj['api_key'])
    body = dict()
    body['enabled'] = enabled
    body['hostName'] = host_name
    res = requests.put(url, data=body, headers=headers)
    print_request_payload(res)


@cli.command()
@click.option('--network_id', prompt=True, required=True, help='This is your meraki network_id')
@click.pass_context
def list_eligible_devices(ctx, network_id):
    url = f'{ctx.obj["base_url"]}/api/v0/networks/{network_id}/wireless/electronicShelfLabel/configuredDevices'
    headers = get_meraki_auth_headers(ctx.obj['api_key'])
    res = requests.get(url, headers=headers)
    print_request_payload(res)


@cli.command()
@click.option('--serial', prompt=True, required=True, help='This is your meraki device serial number')
@click.pass_context
def get_device_settings(ctx, serial):
    url = f'{ctx.obj["base_url"]}/api/v0/devices/{serial}/wireless/electronicShelfLabel'
    headers = get_meraki_auth_headers(ctx.obj['api_key'])
    res = requests.get(url, headers=headers)
    print_request_payload(res)


@cli.command()
@click.option('--serial', prompt=True, required=True, help='This is your meraki device serial number')
@click.option('--enabled', prompt=True, required=True, help='This is enabled/disabled')
@click.option('--channel', prompt=True, required=True, help='This is the channel')
@click.pass_context
def edit_device_settings(ctx, serial, enabled, channel):
    url = f'{ctx.obj["base_url"]}/api/v0/devices/{serial}/wireless/electronicShelfLabel'
    headers = get_meraki_auth_headers(ctx.obj['api_key'])
    body = dict()
    body['enabled'] = enabled
    body['channel'] = channel
    res = requests.put(url, data=body, headers=headers)
    print_request_payload(res)


if __name__ == '__main__':
    cli(obj={})
