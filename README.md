# Get EUDA data - A Home Assistant custom component using the get_euda_data library to add integration to read data for your car from the EU Data Act portal of Volkswagen group 

This integration for Home Assistant will fetch data from the EU Data Act servers related to your car.
The scan_interval is how often the integration should fetch data from the servers, if there's no new data from the car then entities won't be updated.

### Supported setups
This integration will only work for your car if you have done the necessary preparation steps.

## Installation

### Installation with HACS
1. Open HACS in Home Assistant.
2. Go to **Integrations**.
3. Click the three-dot menu in the top right and select **Custom repositories**.
4. Add `https://github.com/bbr111/ha_get_euda_data` and select **Integration** as the category.
5. Click **Add**.
6. Search for `ha_get_euda_data` in HACS and install it.
7. Restart Home Assistant.
8. Add the integration via **Settings -> Devices & Services**.

### Manual installation
Clone or copy the repository and copy the folder 'ha_get_euda_data/custom_components/get_euda_data' into '<config dir>/custom_components'

## Configure

### Configuration options
The integration options can be changed after setup by clicking on the "CONFIGURE" text on the integration.
The options available are:

* **Poll frequency** The interval (in seconds) that the servers are polled for updated data. Please don't use values below 300 seconds, better 600 or 900 seconds.
 
* **Full API debug logging** Enable full debug logging. This will print the full respones from API to homeassistant.log. Only enable for troubleshooting since it will generate a lot of logs.

* **Resources to monitor** Select which resources you wish to monitor for the vehicle.

## Enable debug logging
For comprehensive debug logging you can add this to your `<config dir>/configuration.yaml`:
```yaml
logger:
  default: info
  logs:
    get_euda_data: debug
    custom_components.get_euda_data: debug
 ```
## Further help or contributions
For questions, further help or contributions you can join the (V.A.G. Connected Cars) Discord server at https://discord.gg/826X9jEtCh
