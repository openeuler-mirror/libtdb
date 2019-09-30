Name: libtdb
Version: 1.3.16
Release: 3
Summary: The Tdb library
License: LGPLv3+
URL: http://tdb.samba.org/
Source: http://samba.org/ftp/tdb/tdb-%{version}.tar.gz

BuildRequires: gcc libxslt docbook-style-xsl
BuildRequires: python2-devel python3-devel
Provides: bundled(libreplace)

%description
Tdb library implements a trivial database.

%package -n tdb-tools
Summary: Developer tools for the Tdb library
Requires: libtdb = %{version}-%{release}

%description -n tdb-tools
Tools to manage Tdb files

%package -n python2-tdb
Summary: Python bindings for the Tdb library
Requires: libtdb = %{version}-%{release}
%{?python_provide:%python_provide python2-tdb}

%description -n python2-tdb
Python bindings for the Tdb library

%package -n python3-tdb
Summary: Python3 bindings for the Tdb library
Requires: libtdb = %{version}-%{release}
%{?python_provide:%python_provide python3-tdb}

%description -n python3-tdb
Python3 bindings for the Tdb library

%package devel
Summary: Header files for Tdb library
Requires: libtdb = %{version}-%{release}
Requires: pkgconfig

%description devel
Header files of the Tdb library to develop programs.

%package help
BuildArch: noarch
Summary: Document for the Tdb library

%description help
Document for the Tdb library

%prep
%autosetup -n tdb-%{version} -p1

%build
pathfix.py -n -p -i %{__python2} buildtools/bin/waf

%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace \
           --extra-python=%{__python3}

%make_build

%check
make %{?_smp_mflags} check

%install
%make_install

find $RPM_BUILD_ROOT -name "*.so*" -exec chmod -c +x {} \;
rm -f $RPM_BUILD_ROOT%{_libdir}/libtdb.a

%files
%{_libdir}/libtdb.so.*

%files -n tdb-tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore

%files -n python2-tdb
%{python2_sitearch}/tdb.so
%{python2_sitearch}/_tdb_text.py*

%files -n python3-tdb
%{python3_sitearch}/__pycache__/_tdb_text.cpython*.py[co]
%{python3_sitearch}/tdb.cpython*.so
%{python3_sitearch}/_tdb_text.py

%files devel
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%files help
%doc docs/README
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbtool.8*
%{_mandir}/man8/tdbrestore.8*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n python2-tdb -p /sbin/ldconfig

%postun -n python2-tdb -p /sbin/ldconfig

%post -n python3-tdb -p /sbin/ldconfig

%postun -n python3-tdb -p /sbin/ldconfig

%changelog
* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.3.16-3
- Package init
