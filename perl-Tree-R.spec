%define upstream_name    Tree-R
%define upstream_version 0.072
Summary:	Perl extension for the Rtree data structure and algorithms
Name:		perl-%{upstream_name}
Version:	0.072
Release:	7
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        	https://github.com/ajolma/Tree-R
Source0:	https://cpan.metacpan.org/authors/id/A/AJ/AJOLMA/Tree-R-0.072.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
%description
R-tree is a data structure for storing and indexing and efficiently looking
up non-zero-size spatial objects.

%prep
%setup -q -n Tree-R-0.072

%build
perl Makefile.PL INSTALLDIRS=vendor
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


