# balance-sheet

Get balance/status of your Spacemesh accounts(wallets) and smeshers.

![balance-sheet screenshot](/screenshot1.png)

Send SMH to `sm1qqqqqqxre24mtprsmuht8gfhu28z95hm22zvrdq34rmr8` if you find this tool to be useful.

## Configuration

You must first edit a `config.json` file that lists the account and smesher addresses that you care about.

```json
{
  "accounts": ["sm1qqqqqqxre24mtprsmuht8gfhu28z95hm22zvrdq34rmr8", "sm1qqqqqqx8jyn52q75hjcwshfkuxkpglg32fdemrsjq8jd0"],
  "smeshers": [
    "0x511660323b54d3a5a06a1bcd1e9bedafcf4d9c1d88221c36628f19a9f671d2db",
    "0x595538d185335a19ffcf084d6f109ce757f63a8f59a2de40542a2b271f84dc04"
  ]
}
```

## Usage

```
python balance-sheet.py
```
