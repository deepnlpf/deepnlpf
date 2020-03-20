"""
    Tests Notification Toast
"""
from deepnlpf.modules.notifications.toast import Toast

toast = Toast()

# msg erro
toast.send_notification('error', "Err", "Mensage err!")

# msg success.
toast.send_notification('success', "Success", "Mensage success!")

# XML generated.
toast.send_notification('lexsedi', "Success", "File XML Generated!")