%global php_libname          fpdi
Name:      php-%{php_libname}
Version:   2.3.4
Release:   1%{?dist}
License:   MIT
Summary:   PHP classes to help read pages from existing PDF documents
Group:     Development/Libraries
URL:       https://www.setasign.com/products/fpdi/

# Upstream uses a troublesome URL for source.  Grab it from the Github reference below.
Source:    https://github.com/Setasign/FPDI/archive/v%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:  php-zlib php-fpdf
BuildRequires:  dos2unix
BuildArch: noarch

%description
FPDI is a collection of PHP classes facilitating developers to read pages 
from existing PDF documents and use them as templates in FPDF, which was 
developed by Olivier Plathey. Apart from a copy of FPDF, FPDI does not 
require any special PHP extensions.


%prep
%setup -qn FPDI-%{version}
dos2unix *.txt
find -type f | xargs chmod -x 
pushd src
dos2unix *.php
popd

%build
%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/php/%{php_libname}
cp -a src/*  %{buildroot}%{_datadir}/php/%{php_libname}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/php/%{php_libname}
%doc *.txt *.md


%changelog
* Mon Oct 12 2020 Bishop <bishopolis@gmail.com> - 2.3.4-1
- Initial Packaging
