Name: libtdb
Version: 1.4.2
Release: 1
Summary: The Tdb library
License: LGPLv3+
URL: http://tdb.samba.org/
Source: http://samba.org/ftp/tdb/tdb-%{version}.tar.gz

BuildRequires: gcc libxslt docbook-style-xsl
BuildRequires: python3-devel
Provides: bundled(libreplace)
Obsoletes: python2-tdb < 1.4.2-1

%description
Tdb library implements a trivial database.

%package -n tdb-tools
Summary: Developer tools for the Tdb library
Requires: libtdb = %{version}-%{release}

%description -n tdb-tools
Tools to manage Tdb files

%package -n python3-tdb
Summary: Python3 bindings for the Tdb library
Requires: libtdb = %{version}-%{release}
%{?python_provide:%python_provide python3-tdb}

%description -n python3-tdb
Python3 bindings for the Tdb library

%package devel
Summary: Header files for Tdb library
Requires: libtdb = %{version}-%{release}

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
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace

%make_build

%check
make %{?_smp_mflags} check

%install
%make_install

%files
%{_libdir}/libtdb.so.*

%files -n tdb-tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore

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

%ldconfig_scriptlets

%changelog
* Sat Feb 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.4.2-1
- update to 1.4.2-1, drop python2 support

* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.3.16-3
- Package init
