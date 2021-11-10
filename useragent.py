# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: C:\Users\Administrator.ACER-PC\Documents\Script PYTHON\proyek\uwu_dev\useragent.py
# Compiled at: 2021-04-12 08:54:19
lover_lama = '2356UVIKER90O0D3V1DG4N5'
lover = '098OIO0I11D3V124T1L4N9'
link_download = 'https://semawur.com/aA11nIayhltn'
import os, sys, base64, subprocess
d = 123

def download():
    data = open('dir/d_passw.txt', 'r').readlines()
    da = len(data)
    z = open('dir/d_pass.txt', 'r').readlines()
    v = len(z)
    if v > da:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print '\x1b[95;1m\n\n               By: Iqbal Dev  \x1b[96;1m'
            print '\x1b[97;1m             +---------------+'
            print '\x1b[93;1m             Tool MBF Premium '
            print '+------------------------------------------+'
            print '\x1b[92;1m    Download File Password Toolsnya Dulu '
            print '\x1b[96;1m+------------------------------------------+'
            raw_input('\x1b[97;1m Tekan Enter Untuk Melanjutkan/Download....')
            subprocess.check_output(['am', 'start', link_download])
            raw_input('\x1b[94;1m\n [L] Tekan Enter Untuk Jalankan Toolsnya...')
        except WindowsError:
            pass


def mas():
    data = open('dir/passw.txt', 'r').readlines()
    da = len(data)
    z = open('dir/pass.txt', 'r').readlines()
    v = len(z)
    try:
        f = raw_input('\n\x1b[92;1m [P] Masukkan Password : \n\x1b[97;1m ==============> ')
        if f == '' or f == ' ':
            try:
                raw_input('\n\x1b[93;1m Passwordnya SALAH ngab!,\n Tekan Enter Untuk unduh Password Di Link ini \n')
                subprocess.check_output(['am', 'start', link_download])
                sys.exit()
            except WindowsError:
                print '\n\x1b[96;1m Silahkan Download manual Lewat Link Berikut..'
                print ' ==> \x1b[95;1m' + link_download
                mas()

        if f == lover:
            try:
                print '\n\x1b[93;1m  Maaf Password Salah.. Silahkan Unduh\n Password Toolsnya Lewat Link Berikut \n'
                raw_input(' Tekan Enter Untuk Mengunduh File Password.. ')
                subprocess.check_output(['am', 'start', link_download])
                divev()
            except WindowsError:
                print '\n\x1b[96;1m Silahkan Download manual Lewat Link Berikut..'
                print ' ==> \x1b[95;1m' + link_download
                mas()

        if f == '0' + lover_lama + '0':
            print '\n Password Sudah Kedaluarsa,\n Silahkan Download lagi yang baru..'
            raw_input('\n Tekan Enter Untuk Mengunduh File Password.. ')
            subprocess.check_output(['am', 'start', link_download])
            divev()
        if f != '0' + lover + '0':
            print '\n\x1b[93;1m Maaf Password Salah.. Silahkan Unduh\n Password Tools nya Lewat Link Berikut.. \n '
            raw_input(' \n Tekan ENTER untuk Untuk Melanjutkan ...')
            divev()
        if f == '0' + lover + '0':
            g = open('dir/pass.txt', 'w')
            g.write('1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n')
            g.close()
            d = open('dir/d_passw.txt', 'w')
            d.write('d\nd\nd\nd\nd\nd\nd\nd\nd\nd\n')
            d.close()
            hps = open('dir/passw.txt', 'w')
            hps.write('')
            hps.close()
            print '\n\x1b[92;1m Mantapppp.... '
            print '\x1b[97;1m \n sukses... \n\x1b[96;1m Selamat menggunakan tools ini kembali\n tanpa harus memasukkan password.\n Trimakasih,\n Gunakan Tools ini dengan bijak Ya Sob :) \n'
            raw_input('\x1b[92;1m\n Tekan Enter Untuk Lanjut!')
            os.system('premium_dev.py' if os.name == 'nt' else 'python2 premium_dev.py')
    except KeyboardInterrupt:
        print '\n\x1b[96;1m Silahkan Download manual Lewat Link Berikut..'
        print ' ==> \x1b[95;1m' + link_download
        mas()
    except WindowsError:
        print '\n\x1b[96;1m Silahkan Download manual Lewat Link Berikut..'
        print ' ==> \x1b[95;1m' + link_download
        mas()


def deviv():
    d = open('dir/passw.txt', 'a')
    d.write('w\n')
    d.close()


def divev():
    data = open('dir/passw.txt', 'r').readlines()
    da = len(data)
    z = open('dir/pass.txt', 'r').readlines()
    v = len(z)
    if v < da:
        try:
            print '\n \x1b[93;1m Kamu udah menggunakan tools ini lebih dari\n yang di tentukan oleh pembuat, Silahkan kamu\n DOWNLOAD Passwordnya Lewat Link Berikut,'
            l = raw_input('\n \x1b[97;1mTekan Enter Untuk Mengunduh Passwordnya\n Lewat Browser ==>')
            h = l.replace('/', '0').replace('0', '101').replace('2', 'v').replace('1', 'X').replace('3', 'DEV')
            ha = base64.b64encode(h)
            subprocess.check_output(['am', 'start', link_download])
            mas()
        except KeyboardInterrupt:
            print '\n\x1b[93;1m Silahkan unduh File Password Lewat Link Berikut..'
            raw_input('  Tekan Enter Untuk Mengunduh File Password.. ')
            subprocess.check_output(['am', 'start', link_download])
        except WindowsError:
            print '\n\x1b[96;1m Silahkan Download manual Lewat Link Berikut..'
            print ' ==> \x1b[95;1m' + link_download
            mas()