%define		plugin		sphinxsearch
Summary:	DokuWiki sphinxsearch plugin
Summary(pl.UTF-8):	Wtyczka sphinxsearch dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	0.3.3
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://launchpad.net/dokuwiki-sphinxsearch/0.3/%{version}/+download/sphinxsearch-%{version}.tar.gz
# Source0-md5:	07448f7d6639431f44013708e577f45d
URL:		http://www.dokuwiki.org/plugin:sphinxsearch
BuildRequires:	rpmbuild(macros) >= 1.520
# for %%undos macro
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki >= 20091225
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
DokuWiki Sphinx Search plugin replaces DokuWiki's built-in search
functionality with the Sphinx Search Engine powered search which gives
high-performance and more relevant search results.

Features

- Google-style results (Results are shown in traditional Google-style:
  title, snippet and address (document path).)
- Filtering by namespaces (Click on namespaces in the results to see
  search only within chosen namespace, or simply use “ “search phrase
  @ns personal:mike:travel”)
- Document sections are indexed separately (This is very useful for
  those who have large pages in DokuWiki)

%prep
%setup -qc
mv %{plugin}/* .
rm %{plugin}/.hg_archival.txt
rm %{plugin}/.htaccess

version=$(awk '/date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
# version check blocker intentionally missing
#	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/{INSTALL,COPYING,changelog,sphinx.conf}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL changelog sphinx.conf
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.php
%{plugindir}/conf
