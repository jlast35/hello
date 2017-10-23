# Builds the hello_world debian  package.  

control := control
ziparg := -Zgzip

package := $(shell grep ^Package $(control) | cut -f2 -d\ )
package_version := $(shell ./auto_package_version ..)
arch := $(shell grep ^Architecture $(control) | cut -f2 -d' ')
package_name := $(package)_$(package_version)_$(arch)

build := $(shell pwd)/$(package_name)
deb := $(build).deb

all:
	# Cleaning out previous build (staging) directory.
	rm -rf $(build)
	
	# Staging debian-specific package files.
	mkdir -p $(build)/DEBIAN
	cp ./$(control) $(build)/DEBIAN/control

	# Change this to whatever custom stuff you want to install
	#-----------------------------------------------------------
	mkdir -p $(build)/usr/local/bin
	cp -p ../hello.sh $(build)/usr/local/bin
	chmod 755 $(build)/usr/local/bin/hello.sh
	#-----------------------------------------------------------

	# Building the .deb package.
	sed -i "s/__VERSION__/$(package_version)/g" $(build)/DEBIAN/control
	@# User jenkins cannot chmod files to root, thus fakeroot.
	fakeroot dpkg-deb $(ziparg) -b $(build) $(deb) 2>&1 | grep -v 'dpkg-deb: warning:' | grep -v 'contains user-defined field'
	@# chown --reference=./Makefile $(deb)
	rm -rf $(build)
	# Done.

clean:
	# Removing temporary build files.
	rm -rf $(build)
	rm -f $(deb)
	rm -f *.deb
	rm -f make.out

