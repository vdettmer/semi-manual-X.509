import yaml
import os

file = "csrs.yaml"
defaults = "defaults.yaml"

def load_default_variables():
  with open(defaults, 'r') as file:
    vars = yaml.safe_load_all(file)
    for var in vars:
      global C
      global ST
      global L
      global O
      global OU
      global emailAddress
      C = str(var['C'])
      ST = str(var['ST'])
      L = str(var['L'])
      O = str(var['O'])
      OU = str(var['OU'])
      emailAddress = str(var['emailAddress'])

def generate_conf(file):
  with open(file, 'r') as file:
    csrs = yaml.safe_load_all(file)
    for csr in csrs:
      name = str(csr['cn'])
      alt = csr['alt']
      os.mkdir(name)
      f = open(name+"/"+name+".conf", "w")
      f.write('[req]\ndistinguished_name = req_distinguished_name\nreq_extensions = v3_req\nprompt = no\n\n[req_distinguished_name]\nC = '+C+'\nST = '+ST+'\nL = '+L+'\nO = '+O+'\nOU = '+OU+'\nCN = '+name+'\nemailAddress = '+emailAddress+'\n\n[v3_req]\nkeyUsage = keyEncipherment, dataEncipherment\nextendedKeyUsage = serverAuth\nsubjectAltName = @alt_names\n\n[alt_names]\nDNS.1 ='+name+'\n')
      f.close
      i = 1
      for altname in alt:
        i = i+1
        f = open(name+"/"+name+".conf", "a")
        f.write("DNS."+str(i)+" = "+altname+"\n")
        f.close

def generate_rsa(file):
  with open(file, 'r') as file:
    keys = yaml.safe_load_all(file)
    for key in keys:
      name = str(key['cn'])
      os.system("openssl genrsa -out "+name+"/"+name+".key 4096")

def create_csr(file):
    with open(file, 'r') as file:
      csrs = yaml.safe_load_all(file)
      for csr in csrs:
        name = str(csr['cn'])
        os.system("openssl req -new -out "+name+"/"+name+".csr -key "+name+"/"+name+".key -config "+name+"/"+name+".conf")

def main():
  load_default_variables()
  generate_conf(file)
  generate_rsa(file)
  create_csr(file)

if __name__ == "__main__":
    main()
