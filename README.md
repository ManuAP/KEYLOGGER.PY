<!-- Keylogger Python -->
<h1>Keylogger Python</h1>

<p>Este es un simple keylogger escrito en Python que registra las pulsaciones de teclas en un archivo y lo envía por correo electrónico.</p>

<h2>Requisitos</h2>

<p>Antes de ejecutar este script, asegúrese de tener instaladas las siguientes dependencias:</p>

<ul>
  <li>smtplib</li>
  <li>time</li>
  <li>email</li>
  <li>pynput</li>
</ul>

<p>Puede instalar estas dependencias utilizando el siguiente comando:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>Uso</h2>

<p>Antes de ejecutar el script, asegúrese de configurar las siguientes variables en el código:</p>

<ul>
  <li><code>passwd</code>: la contraseña de la cuenta de correo electrónico desde la que desea enviar el correo electrónico.</li>
  <li><code>msg['From']</code>: la dirección de correo electrónico desde la que desea enviar el correo electrónico.</li>
  <li><code>msg['To']</code>: la dirección de correo electrónico a la que desea enviar el correo electrónico.</li>
</ul>

<p>Una vez que haya configurado las variables, puede ejecutar el script utilizando el siguiente comando:</p>

<pre><code>python keylogger.py</code></pre>

<p>El script registrará las pulsaciones de teclas y las almacenará en un archivo de registro llamado <code>log.txt</code>. Cuando se registren más de 50 pulsaciones de teclas, el archivo de registro se enviará por correo electrónico y se borrará.</p>

<h2>Notas</h2>

<p>Es importante tener en cuenta que el keylogging puede no ser legal en algunos casos y que puede ser considerado una invasión de la privacidad. Es importante asegurarse de tener permiso para utilizar este tipo de software y de no infringir ninguna ley o regulación en el proceso.</p>
