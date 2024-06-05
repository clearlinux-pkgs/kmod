#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v12
# autospec commit: fbcebd0b3d28
#
Name     : kmod
Version  : 31
Release  : 51
URL      : https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-31.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-31.tar.xz
Summary  : Library to deal with kernel modules
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: kmod-bin = %{version}-%{release}
Requires: kmod-data = %{version}-%{release}
Requires: kmod-lib = %{version}-%{release}
Requires: kmod-license = %{version}-%{release}
Requires: kmod-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : file
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : git
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libcrypto)
BuildRequires : pkgconfig(32liblzma)
BuildRequires : pkgconfig(32libzstd)
BuildRequires : pkgconfig(32zlib)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libkmod - linux kernel module handling library
ABSTRACT
========
libkmod was created to allow programs to easily insert, remove and
list modules, also checking its properties, dependencies and aliases.

%package bin
Summary: bin components for the kmod package.
Group: Binaries
Requires: kmod-data = %{version}-%{release}
Requires: kmod-license = %{version}-%{release}

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
Requires: kmod-lib = %{version}-%{release}
Requires: kmod-bin = %{version}-%{release}
Requires: kmod-data = %{version}-%{release}
Provides: kmod-devel = %{version}-%{release}
Requires: kmod = %{version}-%{release}

%description dev
dev components for the kmod package.


%package dev32
Summary: dev32 components for the kmod package.
Group: Default
Requires: kmod-lib32 = %{version}-%{release}
Requires: kmod-bin = %{version}-%{release}
Requires: kmod-data = %{version}-%{release}
Requires: kmod-dev = %{version}-%{release}

%description dev32
dev32 components for the kmod package.


%package lib
Summary: lib components for the kmod package.
Group: Libraries
Requires: kmod-data = %{version}-%{release}
Requires: kmod-license = %{version}-%{release}

%description lib
lib components for the kmod package.


%package lib32
Summary: lib32 components for the kmod package.
Group: Default
Requires: kmod-data = %{version}-%{release}
Requires: kmod-license = %{version}-%{release}

%description lib32
lib32 components for the kmod package.


%package license
Summary: license components for the kmod package.
Group: Default

%description license
license components for the kmod package.


%package man
Summary: man components for the kmod package.
Group: Default

%description man
man components for the kmod package.


%prep
%setup -q -n kmod-31
cd %{_builddir}/kmod-31
pushd ..
cp -a kmod-31 build32
popd
pushd ..
cp -a kmod-31 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1717615761
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-tools \
--disable-test-modules \
--with-zstd
make  %{?_smp_mflags}  LIBS=-lpthread

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-tools \
--disable-test-modules \
--with-zstd   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  LIBS=-lpthread
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-tools \
--disable-test-modules \
--with-zstd
make  %{?_smp_mflags}  LIBS=-lpthread
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1717615761
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmod
cp %{_builddir}/kmod-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kmod/545f380fb332eb41236596500913ff8d582e3ead || :
cp %{_builddir}/kmod-%{version}/libkmod/COPYING %{buildroot}/usr/share/package-licenses/kmod/545f380fb332eb41236596500913ff8d582e3ead || :
cp %{_builddir}/kmod-%{version}/testsuite/COPYING %{buildroot}/usr/share/package-licenses/kmod/545f380fb332eb41236596500913ff8d582e3ead || :
cp %{_builddir}/kmod-%{version}/tools/COPYING %{buildroot}/usr/share/package-licenses/kmod/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
ln -s kmod %{buildroot}/usr/bin/depmod
ln -s kmod %{buildroot}/usr/bin/insmod
ln -s kmod %{buildroot}/usr/bin/lsmod
ln -s kmod %{buildroot}/usr/bin/modinfo
ln -s kmod %{buildroot}/usr/bin/modprobe
ln -s kmod %{buildroot}/usr/bin/rmmod
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kmod
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
/usr/include/libkmod.h
/usr/lib64/libkmod.so
/usr/lib64/pkgconfig/libkmod.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libkmod.so
/usr/lib32/pkgconfig/32libkmod.pc
/usr/lib32/pkgconfig/libkmod.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkmod.so.2.4.1
/usr/lib64/libkmod.so.2
/usr/lib64/libkmod.so.2.4.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libkmod.so.2
/usr/lib32/libkmod.so.2.4.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmod/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/kmod/545f380fb332eb41236596500913ff8d582e3ead

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/depmod.d.5
/usr/share/man/man5/modprobe.d.5
/usr/share/man/man5/modules.dep.5
/usr/share/man/man5/modules.dep.bin.5
/usr/share/man/man8/depmod.8
/usr/share/man/man8/insmod.8
/usr/share/man/man8/kmod.8
/usr/share/man/man8/lsmod.8
/usr/share/man/man8/modinfo.8
/usr/share/man/man8/modprobe.8
/usr/share/man/man8/rmmod.8
