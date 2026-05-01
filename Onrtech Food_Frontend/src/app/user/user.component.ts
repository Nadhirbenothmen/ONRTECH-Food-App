import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { UserAuthService } from '../_Services/user-auth.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  @ViewChild('dashboardIframe') dashboardIframe!: ElementRef<HTMLIFrameElement>;
  
  consumerDashboardUrl: SafeResourceUrl | null = null;
  isLoading = true;
  userName: string = '';

  constructor(
    private sanitizer: DomSanitizer,
    private userAuthService: UserAuthService
  ) {}

  ngOnInit(): void {
    // Get username from localStorage or use default
    this.userName = localStorage.getItem('userName') || 'Usuario';
    this.loadConsumerDashboard();
  }

  loadConsumerDashboard(): void {
    // Replace with your Power BI consumer dashboard URL
    // The Power BI dashboard should contain navigation between multiple reports
    const powerBiUrl = "https://app.fabric.microsoft.com/reportEmbed?reportId=3bb99e5d-fb59-419d-b7c8-118b98e02507&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730&navContentPaneEnabled=false&filterPaneEnabled=false&toolbarPaneEnabled=false"


      

    this.consumerDashboardUrl = this.sanitizer.bypassSecurityTrustResourceUrl(powerBiUrl);
  }

  onIframeLoad(): void {
    this.isLoading = false;
  }

  refreshDashboard(): void {
    this.isLoading = true;
    // Force reload by setting to null and then back
    const currentUrl = this.consumerDashboardUrl;
    this.consumerDashboardUrl = null;
    
    setTimeout(() => {
      this.consumerDashboardUrl = currentUrl;
    }, 100);
  }

  toggleFullscreen(): void {
    const wrapper = document.getElementById('dashboardWrapper');
    
    if (!wrapper) {
      console.error('Dashboard wrapper not found');
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
  
}
