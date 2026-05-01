import { Component, OnInit } from '@angular/core';
import { UserService } from '../_Services/user.service';
import { ToastrService } from 'ngx-toastr';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {

  consumers: any[] = [];
  loading: boolean = false;
  
  // Dashboard properties
  adminDashboardUrl: SafeResourceUrl | null = null;
  isDashboardLoading: boolean = true;
  showDashboard: boolean = false;
  
  // Modal properties
  showModal: boolean = false;
  modalTitle: string = '';
  modalMessage: string = '';
  modalType: 'danger' | 'warning' | 'info' = 'warning';
  modalConfirmText: string = 'Confirm';
  modalCancelText: string = 'Cancel';
  pendingAction: (() => void) | null = null;

  constructor(
    private userService: UserService,
    private toastr: ToastrService,
    private sanitizer: DomSanitizer
  ) { }

  ngOnInit(): void {
    this.loadConsumers();
    this.loadAdminDashboard();
  }

  loadAdminDashboard(): void {
    // Load the complete dashboard with all reports for admin
    const powerBiUrl = 'https://app.fabric.microsoft.com/reportEmbed?reportId=3bb99e5d-fb59-419d-b7c8-118b98e02507&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730&navContentPaneEnabled=false&filterPaneEnabled=false&toolbarPaneEnabled=false';
    this.adminDashboardUrl = this.sanitizer.bypassSecurityTrustResourceUrl(powerBiUrl);
  }

  onDashboardLoad(): void {
    this.isDashboardLoading = false;
  }

  toggleDashboard(): void {
    this.showDashboard = !this.showDashboard;
    if (this.showDashboard) {
      this.isDashboardLoading = true;
    }
  }

  toggleAdminFullscreen(): void {
    const wrapper = document.getElementById('adminDashboardWrapper');
    
    if (!wrapper) {
      console.error('Admin dashboard wrapper not found');
      return;
    }

    if (!document.fullscreenElement) {
      // Enter fullscreen
      if (wrapper.requestFullscreen) {
        wrapper.requestFullscreen();
      } else if ((wrapper as any).webkitRequestFullscreen) {
        (wrapper as any).webkitRequestFullscreen();
      } else if ((wrapper as any).mozRequestFullScreen) {
        (wrapper as any).mozRequestFullScreen();
      } else if ((wrapper as any).msRequestFullscreen) {
        (wrapper as any).msRequestFullscreen();
      }
    } else {
      // Exit fullscreen
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if ((document as any).webkitExitFullscreen) {
        (document as any).webkitExitFullscreen();
      } else if ((document as any).mozCancelFullScreen) {
        (document as any).mozCancelFullScreen();
      } else if ((document as any).msExitFullscreen) {
        (document as any).msExitFullscreen();
      }
    }
  }

  getActiveCount(): number {
    return this.consumers.filter(c => c.activated).length;
  }

  getInactiveCount(): number {
    return this.consumers.filter(c => !c.activated).length;
  }

  loadConsumers() {
    this.loading = true;
    console.log('Loading consumers - loading state:', this.loading);
    
    this.userService.getConsumers().subscribe(
      (res: any) => {
        console.log('Consumers API response:', res);
        this.consumers = res;
        this.loading = false;
        console.log('Consumers loaded successfully. Count:', this.consumers.length);
        console.log('Loading state set to:', this.loading);
      },
      err => {
        console.error('Error loading consumers:', err);
        console.error('Error details:', err.status, err.statusText, err.error);
        this.toastr.error('Failed to load consumers', 'Error');
        this.loading = false;
        console.log('Loading state set to false after error');
      }
    );
  }

  activateUser(userName: string, currentStatus: boolean) {
    const action = currentStatus ? 'deactivate' : 'activate';
    const actionCapitalized = action.charAt(0).toUpperCase() + action.slice(1);
    
    // Set modal properties
    this.modalType = 'warning';
    this.modalTitle = actionCapitalized + ' User';
    this.modalMessage = currentStatus 
      ? `Are you sure you want to <strong>deactivate</strong> user "<strong>${userName}</strong>"?<br><br>The user will not be able to log in until reactivated.`
      : `Are you sure you want to <strong>activate</strong> user "<strong>${userName}</strong>"?<br><br>The user will be able to log in after activation.`;
    this.modalConfirmText = actionCapitalized;
    this.modalCancelText = 'Cancel';
    
    // Store the action to execute on confirmation
    this.pendingAction = () => {
      this.userService.activateUser(userName).subscribe(
        (res: any) => {
          this.toastr.success(
            `User ${userName} has been ${action}d successfully!`,
            actionCapitalized + 'd',
            { timeOut: 3000, progressBar: true, closeButton: true }
          );
          this.loadConsumers();
        },
        err => {
          console.error('Error activating user:', err);
          this.toastr.error(
            `Failed to ${action} user ${userName}`,
            'Error',
            { timeOut: 3000, progressBar: true, closeButton: true }
          );
        }
      );
    };
    
    // Show the modal
    this.showModal = true;
  }

  deleteUser(userName: string) {
    // Set modal properties for delete
    this.modalType = 'danger';
    this.modalTitle = '⚠️ Delete User';
    this.modalMessage = `Are you sure you want to <strong>permanently delete</strong> user "<strong>${userName}</strong>"?<br><br>This action <strong>CANNOT be undone</strong> and will remove:<br>• User account<br>• All associated data<br>• Access permissions`;
    this.modalConfirmText = 'Delete';
    this.modalCancelText = 'Cancel';
    
    // Store the action to execute on confirmation
    this.pendingAction = () => {
      this.userService.deleteUser(userName).subscribe(
        (res: any) => {
          // Backend returns a plain string: "User deleted: username"
          console.log('Delete response:', res);
          this.toastr.success(
            `User ${userName} has been permanently deleted!`,
            'Deleted',
            { timeOut: 4000, progressBar: true, closeButton: true }
          );
          this.loadConsumers();
        },
        err => {
          console.error('Error deleting user:', err);
          this.toastr.error(
            err.error?.message || `Failed to delete user ${userName}`,
            'Error',
            { timeOut: 3000, progressBar: true, closeButton: true }
          );
        }
      );
    };
    
    // Show the modal
    this.showModal = true;
  }
  
  onModalConfirm() {
    if (this.pendingAction) {
      this.pendingAction();
      this.pendingAction = null;
    }
    this.showModal = false;
  }
  
  onModalCancel() {
    this.pendingAction = null;
    this.showModal = false;
  }

}
