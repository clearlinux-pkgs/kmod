#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kmod
Version  : 22
Release  : 21
URL      : https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-22.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-22.tar.xz
Summary  : Library to deal with kernel modules
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: kmod-bin
Requires: kmod-lib
Requires: kmod-data
Requires: kmod-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : gettext-bin
BuildRequires : git
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : sed
Patch1: 0001-kmod-Install-legacy-scripts.patch

%description
kmod - Linux kernel module handling
Information
===========
Build status:
[![Build Status](https://semaphoreci.com/api/v1/projects/29d989ba-0f70-4006-be21-550f6692b73b/449920/shields_badge.svg)](https://semaphoreci.com/lucasdemarchi/kmod)

%package bin
Summary: bin components for the kmod package.
Group: Binaries
Requires: kmod-data

%description bin
bin components for the kmod package.


%package data
Summary: data components for the kmod package.
Group: Data

%description data
data components for the kmod package.


%package dev
Summary: dev components for the kmod package.
Group: Development
Requires: kmod-lib
Requires: kmod-bin
Requires: kmod-data
Provides: kmod-devel

%description dev
dev components for the kmod package.


%package doc
Summary: doc components for the kmod package.
Group: Documentation

%description doc
doc components for the kmod package.


%package lib
Summary: lib components for the kmod package.
Group: Libraries
Requires: kmod-data

%description lib
lib components for the kmod package.


%prep
%setup -q -n kmod-22
%patch1 -p1

%build
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%reconfigure --disable-static --enable-tools --disable-test-modules
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/depmod
/usr/bin/insmod
/usr/bin/kmod
/usr/bin/lsmod
/usr/bin/modinfo
/usr/bin/modprobe
/usr/bin/rmmod

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/kmod

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
