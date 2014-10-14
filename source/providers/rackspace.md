---
defaults:
  image:
    id: e19a734c-c7e6-443a-830c-242209c4d65d
  location:
    id: ORD
    name: Chicago (US)
locations:
- country: US
  id: DFW
  name: Dallas (Texas)
- country: US
  id: ORD
  name: Chicago (Illinois)
- country: US
  id: IAD
  name: Northern Virginia
- country: UK
  id: LON
  name: London (UK)
- country: Australia
  id: SYD
  name: Sydney (Australia)
- country: China
  id: HKG
  name: Hong Kong (China)
sizes:
- bandwidth: null
  disk: 20
  id: '2'
  name: 512MB Standard Instance
  price: 0.022
  price_per: hour
  ram: 512
- bandwidth: null
  disk: 40
  id: '3'
  name: 1GB Standard Instance
  price: 0.06
  price_per: hour
  ram: 1024
- bandwidth: null
  disk: 80
  id: '4'
  name: 2GB Standard Instance
  price: 0.12
  price_per: hour
  ram: 2048
- bandwidth: null
  disk: 160
  id: '5'
  name: 4GB Standard Instance
  price: 0.24
  price_per: hour
  ram: 4096
- bandwidth: null
  disk: 320
  id: '6'
  name: 8GB Standard Instance
  price: 0.48
  price_per: hour
  ram: 8192
- bandwidth: null
  disk: 620
  id: '7'
  name: 15GB Standard Instance
  price: 0.96
  price_per: hour
  ram: 15360
- bandwidth: null
  disk: 1200
  id: '8'
  name: 30GB Standard Instance
  price: 1.2
  price_per: hour
  ram: 30720
- bandwidth: null
  disk: 20
  id: performance1-1
  name: 1 GB Performance
  price: 0.04
  price_per: hour
  ram: 1024
- bandwidth: null
  disk: 40
  id: performance1-2
  name: 2 GB Performance
  price: 0.08
  price_per: hour
  ram: 2048
- bandwidth: null
  disk: 40
  id: performance1-4
  name: 4 GB Performance
  price: 0.16
  price_per: hour
  ram: 4096
- bandwidth: null
  disk: 40
  id: performance1-8
  name: 8 GB Performance
  price: 0.32
  price_per: hour
  ram: 8192
- bandwidth: null
  disk: 40
  id: performance2-120
  name: 120 GB Performance
  price: 5.44
  price_per: hour
  ram: 122880
- bandwidth: null
  disk: 40
  id: performance2-15
  name: 15 GB Performance
  price: 0.68
  price_per: hour
  ram: 15360
- bandwidth: null
  disk: 40
  id: performance2-30
  name: 30 GB Performance
  price: 1.36
  price_per: hour
  ram: 30720
- bandwidth: null
  disk: 40
  id: performance2-60
  name: 60 GB Performance
  price: 2.72
  price_per: hour
  ram: 61440
- bandwidth: null
  disk: 40
  id: performance2-90
  name: 90 GB Performance
  price: 4.08
  price_per: hour
  ram: 92160
template: provider.html
title: Rackspace

---
[Rackspace](http://rackspace.com) is a managed cloud computing company base in Texas with datacenters in Texas, Illinois, Virginia, the United Kingdom, Australia, and Hong Kong.

<em>Don't have a Rackspace account yet? <a href='https://www.rackspace.com/' target='_blank'>Sign up for an account</a>.</em>

## Example

The following [node file](http://docs.devo.ps/manual/nodes/#node-file) will create a 512MB Standard Instance (`size: 2`) on Rackspace in their Dallas datacenter (`location: DFW`):

    id: rackspace_server
    name: Rackspace server
    type: server

    provider:
      name: rackspace
      location: DFW
      size: 2

<em>Note that all the location's ID must be UPPERCASE</em>

<em>The `performance` sizes are only available in the following locations: `IAD`, `ORD`, `LON`.</em>