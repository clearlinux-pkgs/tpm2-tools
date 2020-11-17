#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x14986F6944B1F72B (imran.desai@intel.com)
#
Name     : tpm2-tools
Version  : 5.0
Release  : 9
URL      : https://github.com/tpm2-software/tpm2-tools/releases/download/5.0/tpm2-tools-5.0.tar.gz
Source0  : https://github.com/tpm2-software/tpm2-tools/releases/download/5.0/tpm2-tools-5.0.tar.gz
Source1  : https://github.com/tpm2-software/tpm2-tools/releases/download/5.0/tpm2-tools-5.0.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: tpm2-tools-bin = %{version}-%{release}
Requires: tpm2-tools-data = %{version}-%{release}
Requires: tpm2-tools-license = %{version}-%{release}
Requires: tpm2-tools-man = %{version}-%{release}
BuildRequires : pandoc
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(tss2-esys)
BuildRequires : pkgconfig(tss2-fapi)
BuildRequires : pkgconfig(tss2-mu)
BuildRequires : pkgconfig(tss2-rc)
BuildRequires : pkgconfig(tss2-sys)
BuildRequires : pkgconfig(tss2-tctildr)
BuildRequires : pkgconfig(uuid)

%description
[![Build Status](https://travis-ci.org/tpm2-software/tpm2-tools.svg?branch=master)](https://travis-ci.org/tpm2-software/tpm2-tools)
[![FreeBSD Build Status](https://api.cirrus-ci.com/github/tpm2-software/tpm2-tools.svg?branch=master)](https://cirrus-ci.com/github/tpm2-software/tpm2-tools)
[![codecov](https://codecov.io/gh/tpm2-software/tpm2-tools/branch/master/graph/badge.svg)](https://codecov.io/gh/tpm2-software/tpm2-tools)
[![Coverity Scan](https://img.shields.io/coverity/scan/3997.svg)](https://scan.coverity.com/projects/01org-tpm2-0-tools)
[![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/tpm2-software/tpm2-tools.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tpm2-software/tpm2-tools/context:cpp)

%package bin
Summary: bin components for the tpm2-tools package.
Group: Binaries
Requires: tpm2-tools-data = %{version}-%{release}
Requires: tpm2-tools-license = %{version}-%{release}

%description bin
bin components for the tpm2-tools package.


%package data
Summary: data components for the tpm2-tools package.
Group: Data

%description data
data components for the tpm2-tools package.


%package license
Summary: license components for the tpm2-tools package.
Group: Default

%description license
license components for the tpm2-tools package.


%package man
Summary: man components for the tpm2-tools package.
Group: Default

%description man
man components for the tpm2-tools package.


%prep
%setup -q -n tpm2-tools-5.0
cd %{_builddir}/tpm2-tools-5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605633679
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1605633679
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tpm2-tools
cp %{_builddir}/tpm2-tools-5.0/doc/LICENSE %{buildroot}/usr/share/package-licenses/tpm2-tools/e8566cc4b6c5a67bda0376f10f71d0df00e262a9
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tpm2
/usr/bin/tpm2_activatecredential
/usr/bin/tpm2_certify
/usr/bin/tpm2_certifyX509certutil
/usr/bin/tpm2_certifycreation
/usr/bin/tpm2_changeauth
/usr/bin/tpm2_changeeps
/usr/bin/tpm2_changepps
/usr/bin/tpm2_checkquote
/usr/bin/tpm2_clear
/usr/bin/tpm2_clearcontrol
/usr/bin/tpm2_clockrateadjust
/usr/bin/tpm2_commit
/usr/bin/tpm2_create
/usr/bin/tpm2_createak
/usr/bin/tpm2_createek
/usr/bin/tpm2_createpolicy
/usr/bin/tpm2_createprimary
/usr/bin/tpm2_dictionarylockout
/usr/bin/tpm2_duplicate
/usr/bin/tpm2_ecdhkeygen
/usr/bin/tpm2_ecdhzgen
/usr/bin/tpm2_ecephemeral
/usr/bin/tpm2_encryptdecrypt
/usr/bin/tpm2_eventlog
/usr/bin/tpm2_evictcontrol
/usr/bin/tpm2_flushcontext
/usr/bin/tpm2_getcap
/usr/bin/tpm2_getcommandauditdigest
/usr/bin/tpm2_geteccparameters
/usr/bin/tpm2_getekcertificate
/usr/bin/tpm2_getrandom
/usr/bin/tpm2_getsessionauditdigest
/usr/bin/tpm2_gettestresult
/usr/bin/tpm2_gettime
/usr/bin/tpm2_hash
/usr/bin/tpm2_hierarchycontrol
/usr/bin/tpm2_hmac
/usr/bin/tpm2_import
/usr/bin/tpm2_incrementalselftest
/usr/bin/tpm2_load
/usr/bin/tpm2_loadexternal
/usr/bin/tpm2_makecredential
/usr/bin/tpm2_nvcertify
/usr/bin/tpm2_nvdefine
/usr/bin/tpm2_nvextend
/usr/bin/tpm2_nvincrement
/usr/bin/tpm2_nvread
/usr/bin/tpm2_nvreadlock
/usr/bin/tpm2_nvreadpublic
/usr/bin/tpm2_nvsetbits
/usr/bin/tpm2_nvundefine
/usr/bin/tpm2_nvwrite
/usr/bin/tpm2_nvwritelock
/usr/bin/tpm2_pcrallocate
/usr/bin/tpm2_pcrevent
/usr/bin/tpm2_pcrextend
/usr/bin/tpm2_pcrread
/usr/bin/tpm2_pcrreset
/usr/bin/tpm2_policyauthorize
/usr/bin/tpm2_policyauthorizenv
/usr/bin/tpm2_policyauthvalue
/usr/bin/tpm2_policycommandcode
/usr/bin/tpm2_policycountertimer
/usr/bin/tpm2_policycphash
/usr/bin/tpm2_policyduplicationselect
/usr/bin/tpm2_policylocality
/usr/bin/tpm2_policynamehash
/usr/bin/tpm2_policynv
/usr/bin/tpm2_policynvwritten
/usr/bin/tpm2_policyor
/usr/bin/tpm2_policypassword
/usr/bin/tpm2_policypcr
/usr/bin/tpm2_policyrestart
/usr/bin/tpm2_policysecret
/usr/bin/tpm2_policysigned
/usr/bin/tpm2_policytemplate
/usr/bin/tpm2_policyticket
/usr/bin/tpm2_print
/usr/bin/tpm2_quote
/usr/bin/tpm2_rc_decode
/usr/bin/tpm2_readclock
/usr/bin/tpm2_readpublic
/usr/bin/tpm2_rsadecrypt
/usr/bin/tpm2_rsaencrypt
/usr/bin/tpm2_selftest
/usr/bin/tpm2_send
/usr/bin/tpm2_setclock
/usr/bin/tpm2_setcommandauditstatus
/usr/bin/tpm2_setprimarypolicy
/usr/bin/tpm2_shutdown
/usr/bin/tpm2_sign
/usr/bin/tpm2_startauthsession
/usr/bin/tpm2_startup
/usr/bin/tpm2_stirrandom
/usr/bin/tpm2_testparms
/usr/bin/tpm2_unseal
/usr/bin/tpm2_verifysignature
/usr/bin/tpm2_zgen2phase
/usr/bin/tss2
/usr/bin/tss2_authorizepolicy
/usr/bin/tss2_changeauth
/usr/bin/tss2_createkey
/usr/bin/tss2_createnv
/usr/bin/tss2_createseal
/usr/bin/tss2_decrypt
/usr/bin/tss2_delete
/usr/bin/tss2_encrypt
/usr/bin/tss2_exportkey
/usr/bin/tss2_exportpolicy
/usr/bin/tss2_getappdata
/usr/bin/tss2_getcertificate
/usr/bin/tss2_getdescription
/usr/bin/tss2_getinfo
/usr/bin/tss2_getplatformcertificates
/usr/bin/tss2_getrandom
/usr/bin/tss2_gettpmblobs
/usr/bin/tss2_import
/usr/bin/tss2_list
/usr/bin/tss2_nvextend
/usr/bin/tss2_nvincrement
/usr/bin/tss2_nvread
/usr/bin/tss2_nvsetbits
/usr/bin/tss2_nvwrite
/usr/bin/tss2_pcrextend
/usr/bin/tss2_pcrread
/usr/bin/tss2_provision
/usr/bin/tss2_quote
/usr/bin/tss2_setappdata
/usr/bin/tss2_setcertificate
/usr/bin/tss2_setdescription
/usr/bin/tss2_sign
/usr/bin/tss2_unseal
/usr/bin/tss2_verifyquote
/usr/bin/tss2_verifysignature
/usr/bin/tss2_writeauthorizenv

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/tpm2
/usr/share/bash-completion/completions/tpm2_completion.bash
/usr/share/bash-completion/completions/tss2
/usr/share/bash-completion/completions/tss2_authorizepolicy
/usr/share/bash-completion/completions/tss2_changeauth
/usr/share/bash-completion/completions/tss2_createkey
/usr/share/bash-completion/completions/tss2_createnv
/usr/share/bash-completion/completions/tss2_createseal
/usr/share/bash-completion/completions/tss2_decrypt
/usr/share/bash-completion/completions/tss2_delete
/usr/share/bash-completion/completions/tss2_encrypt
/usr/share/bash-completion/completions/tss2_exportkey
/usr/share/bash-completion/completions/tss2_exportpolicy
/usr/share/bash-completion/completions/tss2_getappdata
/usr/share/bash-completion/completions/tss2_getcertificate
/usr/share/bash-completion/completions/tss2_getdescription
/usr/share/bash-completion/completions/tss2_getinfo
/usr/share/bash-completion/completions/tss2_getplatformcertificates
/usr/share/bash-completion/completions/tss2_getrandom
/usr/share/bash-completion/completions/tss2_gettpmblobs
/usr/share/bash-completion/completions/tss2_import
/usr/share/bash-completion/completions/tss2_list
/usr/share/bash-completion/completions/tss2_nvextend
/usr/share/bash-completion/completions/tss2_nvincrement
/usr/share/bash-completion/completions/tss2_nvread
/usr/share/bash-completion/completions/tss2_nvsetbits
/usr/share/bash-completion/completions/tss2_nvwrite
/usr/share/bash-completion/completions/tss2_pcrextend
/usr/share/bash-completion/completions/tss2_pcrread
/usr/share/bash-completion/completions/tss2_provision
/usr/share/bash-completion/completions/tss2_quote
/usr/share/bash-completion/completions/tss2_setappdata
/usr/share/bash-completion/completions/tss2_setcertificate
/usr/share/bash-completion/completions/tss2_setdescription
/usr/share/bash-completion/completions/tss2_sign
/usr/share/bash-completion/completions/tss2_unseal
/usr/share/bash-completion/completions/tss2_verifyquote
/usr/share/bash-completion/completions/tss2_verifysignature
/usr/share/bash-completion/completions/tss2_writeauthorizenv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tpm2-tools/e8566cc4b6c5a67bda0376f10f71d0df00e262a9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tpm2.1
/usr/share/man/man1/tpm2_activatecredential.1
/usr/share/man/man1/tpm2_certify.1
/usr/share/man/man1/tpm2_certifyX509certutil.1
/usr/share/man/man1/tpm2_certifycreation.1
/usr/share/man/man1/tpm2_changeauth.1
/usr/share/man/man1/tpm2_changeeps.1
/usr/share/man/man1/tpm2_changepps.1
/usr/share/man/man1/tpm2_checkquote.1
/usr/share/man/man1/tpm2_clear.1
/usr/share/man/man1/tpm2_clearcontrol.1
/usr/share/man/man1/tpm2_clockrateadjust.1
/usr/share/man/man1/tpm2_commit.1
/usr/share/man/man1/tpm2_create.1
/usr/share/man/man1/tpm2_createak.1
/usr/share/man/man1/tpm2_createek.1
/usr/share/man/man1/tpm2_createpolicy.1
/usr/share/man/man1/tpm2_createprimary.1
/usr/share/man/man1/tpm2_dictionarylockout.1
/usr/share/man/man1/tpm2_duplicate.1
/usr/share/man/man1/tpm2_ecdhkeygen.1
/usr/share/man/man1/tpm2_ecdhzgen.1
/usr/share/man/man1/tpm2_ecephemeral.1
/usr/share/man/man1/tpm2_encryptdecrypt.1
/usr/share/man/man1/tpm2_eventlog.1
/usr/share/man/man1/tpm2_evictcontrol.1
/usr/share/man/man1/tpm2_flushcontext.1
/usr/share/man/man1/tpm2_getcap.1
/usr/share/man/man1/tpm2_getcommandauditdigest.1
/usr/share/man/man1/tpm2_geteccparameters.1
/usr/share/man/man1/tpm2_getekcertificate.1
/usr/share/man/man1/tpm2_getrandom.1
/usr/share/man/man1/tpm2_getsessionauditdigest.1
/usr/share/man/man1/tpm2_gettestresult.1
/usr/share/man/man1/tpm2_gettime.1
/usr/share/man/man1/tpm2_hash.1
/usr/share/man/man1/tpm2_hierarchycontrol.1
/usr/share/man/man1/tpm2_hmac.1
/usr/share/man/man1/tpm2_import.1
/usr/share/man/man1/tpm2_incrementalselftest.1
/usr/share/man/man1/tpm2_load.1
/usr/share/man/man1/tpm2_loadexternal.1
/usr/share/man/man1/tpm2_makecredential.1
/usr/share/man/man1/tpm2_nvcertify.1
/usr/share/man/man1/tpm2_nvdefine.1
/usr/share/man/man1/tpm2_nvextend.1
/usr/share/man/man1/tpm2_nvincrement.1
/usr/share/man/man1/tpm2_nvread.1
/usr/share/man/man1/tpm2_nvreadlock.1
/usr/share/man/man1/tpm2_nvreadpublic.1
/usr/share/man/man1/tpm2_nvsetbits.1
/usr/share/man/man1/tpm2_nvundefine.1
/usr/share/man/man1/tpm2_nvwrite.1
/usr/share/man/man1/tpm2_nvwritelock.1
/usr/share/man/man1/tpm2_pcrallocate.1
/usr/share/man/man1/tpm2_pcrevent.1
/usr/share/man/man1/tpm2_pcrextend.1
/usr/share/man/man1/tpm2_pcrread.1
/usr/share/man/man1/tpm2_pcrreset.1
/usr/share/man/man1/tpm2_policyauthorize.1
/usr/share/man/man1/tpm2_policyauthorizenv.1
/usr/share/man/man1/tpm2_policyauthvalue.1
/usr/share/man/man1/tpm2_policycommandcode.1
/usr/share/man/man1/tpm2_policycountertimer.1
/usr/share/man/man1/tpm2_policycphash.1
/usr/share/man/man1/tpm2_policyduplicationselect.1
/usr/share/man/man1/tpm2_policylocality.1
/usr/share/man/man1/tpm2_policynamehash.1
/usr/share/man/man1/tpm2_policynv.1
/usr/share/man/man1/tpm2_policynvwritten.1
/usr/share/man/man1/tpm2_policyor.1
/usr/share/man/man1/tpm2_policypassword.1
/usr/share/man/man1/tpm2_policypcr.1
/usr/share/man/man1/tpm2_policyrestart.1
/usr/share/man/man1/tpm2_policysecret.1
/usr/share/man/man1/tpm2_policysigned.1
/usr/share/man/man1/tpm2_policytemplate.1
/usr/share/man/man1/tpm2_policyticket.1
/usr/share/man/man1/tpm2_print.1
/usr/share/man/man1/tpm2_quote.1
/usr/share/man/man1/tpm2_rc_decode.1
/usr/share/man/man1/tpm2_readclock.1
/usr/share/man/man1/tpm2_readpublic.1
/usr/share/man/man1/tpm2_rsadecrypt.1
/usr/share/man/man1/tpm2_rsaencrypt.1
/usr/share/man/man1/tpm2_selftest.1
/usr/share/man/man1/tpm2_send.1
/usr/share/man/man1/tpm2_setclock.1
/usr/share/man/man1/tpm2_setcommandauditstatus.1
/usr/share/man/man1/tpm2_setprimarypolicy.1
/usr/share/man/man1/tpm2_shutdown.1
/usr/share/man/man1/tpm2_sign.1
/usr/share/man/man1/tpm2_startauthsession.1
/usr/share/man/man1/tpm2_startup.1
/usr/share/man/man1/tpm2_stirrandom.1
/usr/share/man/man1/tpm2_testparms.1
/usr/share/man/man1/tpm2_unseal.1
/usr/share/man/man1/tpm2_verifysignature.1
/usr/share/man/man1/tpm2_zgen2phase.1
/usr/share/man/man1/tss2_authorizepolicy.1
/usr/share/man/man1/tss2_changeauth.1
/usr/share/man/man1/tss2_createkey.1
/usr/share/man/man1/tss2_createnv.1
/usr/share/man/man1/tss2_createseal.1
/usr/share/man/man1/tss2_decrypt.1
/usr/share/man/man1/tss2_delete.1
/usr/share/man/man1/tss2_encrypt.1
/usr/share/man/man1/tss2_exportkey.1
/usr/share/man/man1/tss2_exportpolicy.1
/usr/share/man/man1/tss2_getappdata.1
/usr/share/man/man1/tss2_getcertificate.1
/usr/share/man/man1/tss2_getdescription.1
/usr/share/man/man1/tss2_getinfo.1
/usr/share/man/man1/tss2_getplatformcertificates.1
/usr/share/man/man1/tss2_getrandom.1
/usr/share/man/man1/tss2_gettpmblobs.1
/usr/share/man/man1/tss2_import.1
/usr/share/man/man1/tss2_list.1
/usr/share/man/man1/tss2_nvextend.1
/usr/share/man/man1/tss2_nvincrement.1
/usr/share/man/man1/tss2_nvread.1
/usr/share/man/man1/tss2_nvsetbits.1
/usr/share/man/man1/tss2_nvwrite.1
/usr/share/man/man1/tss2_pcrextend.1
/usr/share/man/man1/tss2_pcrread.1
/usr/share/man/man1/tss2_provision.1
/usr/share/man/man1/tss2_quote.1
/usr/share/man/man1/tss2_setappdata.1
/usr/share/man/man1/tss2_setcertificate.1
/usr/share/man/man1/tss2_setdescription.1
/usr/share/man/man1/tss2_sign.1
/usr/share/man/man1/tss2_unseal.1
/usr/share/man/man1/tss2_verifyquote.1
/usr/share/man/man1/tss2_verifysignature.1
/usr/share/man/man1/tss2_writeauthorizenv.1
