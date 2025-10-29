require 'openssl'

def encrypt_file(file_path, password)
  cipher = OpenSSL::Cipher::AES.new(256, :CBC)
  cipher.encrypt
  key = OpenSSL::PKCS5.pbkdf2_hmac_sha1(password, "salt", 20000, cipher.key_len)
  cipher.key = key
  iv = cipher.random_iv
  File.open(file_path + ".enc", "wb") do |f|
    f.write(iv)
    File.open(file_path, "rb") do |inf|
      while chunk = inf.read(1024)
        f.write(cipher.update(chunk))
      end
      f.write(cipher.final)
    end
  end
  puts "File encrypted"
end

puts "Enter file path to encrypt: "
file_path = gets.chomp
puts "Enter password: "
password = gets.chomp
encrypt_file(file_path, password)
