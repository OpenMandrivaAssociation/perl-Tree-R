%define upstream_name    Tree-R
Summary:	Perl extension for the Rtree data structure and algorithms
Name:		perl-%{upstream_name}
Version:	0.072
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        	https://github.com/ajolma/Tree-R
Source0:    	https://cpan.metacpan.org/authors/id/A/AJ/AJOLMA/Tree-R-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
%description
R-tree is a data structure for storing and indexing and efficiently looking
up non-zero-size spatial objects.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root) 
%doc Changes README
%{perl_vendorlib}/Tree/R.pm
%{perl_vendorlib}/auto/Tree/R
%{_mandir}/man3/Tree::R.3pm.*


%changelog
* Thu Nov 04 2010 Jani Välimaa <wally@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 593399
- use perl_convert_version macro
- fix summary, description, license, source and URL
- tag package as noarch
- install files to a correct location

* Sun Oct 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.06-1mdv2011.0
+ Revision: 591223
- import perl-Tree-R

