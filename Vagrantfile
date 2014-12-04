# -*- mode: ruby; -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 8001, host: 8001
  config.ssh.forward_agent = true

  config.vm.synced_folder "./invoice", "/home/vagrant/invoice"
  config.vm.synced_folder "./staticfiles", "/home/vagrant/staticfiles"


  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.customize ["modifyvm", :id, "--memory", "1012"]
  end

end
