%global		priority	65-2
%global		fontname	ipa-pmincho
%global		fontconf	%{priority}-%{fontname}.conf
%global		archiveversion	00303
%global		archivename	ipamp%{archiveversion}

Name:		%{fontname}-fonts
Version:	003.03
Release:	4%{?dist}
Summary:	Japanese Proportional Mincho-typeface OpenType font by IPA

Group:		User Interface/X
License:	IPA
URL:		http://ossipedia.ipa.go.jp/ipafont/
Source0:	http://info.openlab.ipa.go.jp/ipafont/fontdata/%{archivename}.zip
Source1:	%{name}-fontconfig.conf

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
IPA Font is a Japanese OpenType fonts that is JIS X 0213:2004
compliant, provided by Information-technology Promotion Agency, Japan.

This package contains Proportional Mincho style font.

%prep
%setup -q -n %{archivename}


%build

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p	%{SOURCE1}	\
			$RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

ln -s	%{_fontconfig_templatedir}/%{fontconf}	\
	$RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc Readme_%{archivename}.txt IPA_Font_License_Agreement_v1.0.txt


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Akira TAGOH <tagoh@redhat.com>
- the spec file cleanup

* Fri Aug 17 2012 Akira TAGOH <tagoh@redhat.com> - 003.03-3
- Enable autohinting explicitly since the own hinting seems broken.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Akira TAGOH <tagoh@redhat.com> - 003.03-1
- New upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 25 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-4
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-3
- Get rid of compare="contains".

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-2
- Get rid of binding="same" from the fontconfig config file. (#578025)

* Tue Feb 16 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-1
- New upstream release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-3
- Disable hinting.

* Wed Apr 22 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-2
- Correct the source URL.

* Tue Apr 21 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-1
- Initial package.

